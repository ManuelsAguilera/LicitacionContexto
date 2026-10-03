#!/usr/bin/env python3
"""Ensambla Markdown por parte, genera HTML corporativo y PDF de revisión/entrega."""
from __future__ import annotations
import argparse, hashlib, html, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
from urllib.parse import quote
from artefactos import ROOT, frontmatter_text, parse_frontmatter, words

THEME=ROOT/"plantillas"/"tema.yml"; CSS=ROOT/"plantillas"/"base.css"

def simple_yaml(path):
    data={}; section=None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"): continue
        m=re.match(r"^(\w+):\s*(.*)$",line)
        if m:
            key,value=m.groups()
            if value: data[key]=value.strip('"\'')
            else: section=key; data[key]={}
        elif section and (m:=re.match(r"^\s+(\w+):\s*(.+)$",line)):
            data[section][m.group(1)]=m.group(2).strip('"\'')
    return data

def inline(text):
    text=html.escape(text,quote=False)
    text=re.sub(r"`([^`]+)`",r"<code>\1</code>",text)
    text=re.sub(r"\*\*(.+?)\*\*",r"<strong>\1</strong>",text)
    text=re.sub(r"\*(.+?)\*",r"<em>\1</em>",text)
    text=re.sub(r"\[([^\]]+)\]\(([^)]+)\)",r'<a href="\2">\1</a>',text)
    return text

def fallback_markdown(markdown):
    out=[]; lines=markdown.splitlines(); i=0
    while i<len(lines):
        line=lines[i]; s=line.strip()
        if not s: i+=1; continue
        if s.startswith("```"):
            lang=s[3:].strip(); code=[]; i+=1
            while i<len(lines) and not lines[i].strip().startswith("```"): code.append(lines[i]); i+=1
            out.append(f'<pre><code class="language-{html.escape(lang)}">{html.escape(chr(10).join(code))}</code></pre>'); i+=1; continue
        if s.startswith(":::"):
            classes=html.escape(s[3:].strip(),quote=True); inner=[]; i+=1
            while i<len(lines) and lines[i].strip()!=":::": inner.append(lines[i]); i+=1
            out.append(f'<div class="{classes}">'+fallback_markdown("\n".join(inner))+"</div>"); i+=1; continue
        if s.startswith("<"):
            raw=[]
            while i<len(lines) and lines[i].strip(): raw.append(lines[i]); i+=1
            out.extend(raw); continue
        if s.startswith("|") and i+1<len(lines) and re.match(r"\s*\|?[\s:|-]+\|",lines[i+1]):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i+=1
            if len(rows)>1: rows.pop(1)
            out.append("<table><thead><tr>"+"".join(f"<th>{inline(c)}</th>" for c in rows[0])+"</tr></thead><tbody>"+"".join("<tr>"+"".join(f"<td>{inline(c)}</td>" for c in r)+"</tr>" for r in rows[1:])+"</tbody></table>"); continue
        hm=re.match(r"^(#{1,6})\s+(.*)$",s)
        if hm:
            level=len(hm.group(1)); title=hm.group(2); slug=re.sub(r"[^a-z0-9]+","-",title.casefold()).strip("-")
            out.append(f'<h{level} id="{slug}">{inline(title)}</h{level}>'); i+=1; continue
        if s.startswith("!["):
            m=re.match(r"!\[([^\]]*)\]\(([^)]+)\)",s)
            if m: out.append(f'<figure><img alt="{html.escape(m.group(1))}" src="{html.escape(m.group(2))}"><figcaption>{inline(m.group(1))}</figcaption></figure>'); i+=1; continue
        if s.startswith("- "):
            items=[]
            while i<len(lines) and lines[i].strip().startswith("- "): items.append("<li>"+inline(lines[i].strip()[2:])+"</li>"); i+=1
            out.append("<ul>"+"".join(items)+"</ul>"); continue
        para=[s]; i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(("#","- ","|","```","<")):
            para.append(lines[i].strip()); i+=1
        out.append("<p>"+" ".join(inline(x) for x in para)+"</p>")
    return "\n".join(out)

def load_part(part):
    folders=list((ROOT/"02_Propuesta").glob(f"sd-{part[3:]}_*"))
    if not folders: raise ValueError(f"No existe carpeta de {part}")
    folder=folders[0]; master=next(folder.glob("sd-*.md"),None)
    if not master: raise ValueError(f"No existe maestro para {part}")
    raw=master.read_text(encoding="utf-8-sig"); fm,body=parse_frontmatter(raw)
    sections=[]
    for line in body.splitlines():
        m=re.match(r"\|\s*(\d+)\s*\|\s*([^|]+)\|\s*`?(sd-\d+_s\d+_[^`|]+\.md)`?\s*\|",line)
        if m: sections.append((int(m.group(1)),m.group(2).strip(),folder/m.group(3).strip("`")))
    declared=fm.get("secciones",[])
    if not sections: raise ValueError(f"{part}: el maestro no declara archivos de sección parseables")
    missing=[str(p.relative_to(ROOT)) for _,_,p in sections if not p.exists()]
    if missing: raise ValueError(f"{part}: faltan secciones materializadas: {', '.join(missing)}")
    ordered=[]
    for n,title,p in sections:
        sfm,content=parse_frontmatter(p.read_text(encoding="utf-8-sig"))
        if sfm.get("estado") not in {"revisado","congelado"}: pass
        if not content.strip(): raise ValueError(f"{p.relative_to(ROOT)} está vacía")
        ordered.append((n,title,p,sfm,content))
    return folder,master,fm,ordered

def corporate_css(theme, part, title):
    css=CSS.read_text(encoding="utf-8")
    colors=theme.get("colores",{})
    for key,original in {"primario":"#102A43","secundario":"#0F766E","acento":"#C58B2A","texto":"#243B53","neutro":"#F0F4F8","menta":"#85C9AF","menta_suave":"#E8F4F1","texto_calido":"#92521C","alerta_suave":"#FBF1E8"}.items():
        if key in colors: css=css.replace(original,colors[key])
    fonts=theme.get("tipografias",{})
    if fonts.get("cuerpo"): css=css.replace("Arial",fonts["cuerpo"])
    if fonts.get("titulo"): css=css.replace("__TITLE_FONT__",fonts["titulo"])
    if fonts.get("marca"): css=css.replace("__BRAND_FONT__",fonts["marca"])
    if fonts.get("monospace"): css=css.replace("Consolas",fonts["monospace"])
    brand=str(theme.get("marca","Only Simple Solutions" )).replace('"','\\"')
    css=css.replace('"Only Simple Solutions"', '"'+brand+'"')
    css=css.replace("__RUNNING_TITLE__",(part+" · "+title).replace('"','\\"'))
    if theme.get("tamano_cuerpo_pt"): css=css.replace("font-size: 11pt",f"font-size: {theme['tamano_cuerpo_pt']}pt")
    if theme.get("tamano_tabla_minimo_pt"): css=css.replace("font-size:9pt",f"font-size:{theme['tamano_tabla_minimo_pt']}pt")
    return css

def render_html(part,title,ordered,theme,draft,output,page_numbers=None,front_only=False,section_only=None):
    metadata=f"{part} · {title}"
    content=[]; toc=[]
    for i,(_,section_title,path,sfm,body) in enumerate(ordered,1):
        _,body=parse_frontmatter(path.read_text(encoding="utf-8-sig"))
        diagrams=re.findall(r"```mermaid\s*\n(.*?)\n```",body,re.S|re.I)
        if diagrams:
            mmdc=shutil.which("mmdc")
            if not mmdc: raise RuntimeError(f"{path.relative_to(ROOT)} contiene Mermaid; se requiere Mermaid CLI (mmdc) para exportarlo como figura")
            for source in diagrams:
                digest=hashlib.sha256(source.encode("utf-8")).hexdigest()[:16]; builddir=ROOT/"05_Gestion"/"build"; builddir.mkdir(parents=True,exist_ok=True)
                mmd=builddir/f"{part}-{digest}.mmd"; svg=builddir/f"{part}-{digest}.svg"
                if not svg.exists():
                    mmd.write_text(source+"\n",encoding="utf-8"); proc=subprocess.run([mmdc,"-i",str(mmd),"-o",str(svg),"-b","transparent"],capture_output=True,text=True,timeout=120)
                    if proc.returncode or not svg.exists(): raise RuntimeError("Mermaid CLI falló: "+proc.stderr[-800:])
                figure=f'<figure class="diagram"><img src="{html.escape(svg.resolve().as_uri(),quote=True)}" alt="Diagrama Mermaid"></figure>'
                body=re.sub(r"```mermaid\s*\n"+re.escape(source)+r"\n```",lambda _:figure,body,count=1,flags=re.I)
        slug=f"seccion-{i}"
        pandoc=shutil.which("pandoc")
        if pandoc:
            proc=subprocess.run([pandoc,"--from=markdown+fenced_divs+pipe_tables","--to=html5","--lua-filter",str(ROOT/"plantillas"/"filtros"/"componentes.lua")],input=body,text=True,capture_output=True,cwd=ROOT)
            if proc.returncode: raise RuntimeError("Pandoc falló: "+proc.stderr[-1200:])
            rendered=proc.stdout
        else:
            rendered=fallback_markdown(body)
        def local_uri(match):
            href=match.group(2)
            if href.startswith(("http:","https:","file:","#","data:")): return match.group(0)
            resolved=(path.parent/href).resolve()
            return f'{match.group(1)}="{html.escape(resolved.as_uri(),quote=True)}"'
        rendered=re.sub(r'(src|href)="([^"]+)"',local_uri,rendered)
        title_escaped=html.escape(section_title)
        has_heading=any(" ".join(re.sub(r"^\d+(?:\.\d+)*\.?\s*", "", html.unescape(m)).casefold().split()) == " ".join(section_title.casefold().split()) for m in re.findall(r"<h1\b[^>]*>(.*?)</h1>",rendered,re.I|re.S))
        if not has_heading: rendered=f'<h1 class="document-title">{title_escaped}</h1>'+rendered
        content.append(f'<section class="section-content" id="{slug}">{rendered}</section>')
        number=(page_numbers or {}).get(slug,"")
        toc.append(f'<li><a href="#{slug}">{title_escaped}</a><span class="page-number">{number}</span></li>')
    watermark='<div class="draft-watermark">BORRADOR</div>' if draft else ''
    logo_uri=(ROOT/"plantillas"/"recursos"/"onlysimplesolutions.png").resolve().as_uri()
    cover=f'<section class="cover"><img class="cover-logo" src="{html.escape(logo_uri,quote=True)}" alt="Logo de Only Simple Solutions"><div class="cover-mark">{html.escape(str(theme.get("marca","Only Simple Solutions")))}</div><h1>{html.escape(title)}</h1><p class="subtitle">Propuesta técnica · Licitación TFEP-01/2026</p><p class="identifier">{part}</p>{watermark}</section>'
    index=f'<nav class="toc"><h1>Índice</h1><ol>{"".join(toc)}</ol></nav>'
    if front_only: body=cover+index
    elif section_only is not None: body=content[section_only]
    else: body=cover+index+"".join(content)
    css=corporate_css(theme,part,title)
    html_doc=f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="author" content="{html.escape(str(theme.get("marca","Only Simple Solutions")),quote=True)}"><meta name="subject" content="Licitación TFEP-01/2026 · {html.escape(part,quote=True)}"><title>{html.escape(metadata)}</title><style>{css}</style></head><body><div class="running-company">{html.escape(str(theme.get("marca","Only Simple Solutions")))}</div>{body}</body></html>'
    output.write_text(html_doc,encoding="utf-8")

def edge_renderer():
    candidates=[Path(os.environ.get("PROGRAMFILES(X86)",r"C:\Program Files (x86)"))/"Microsoft/Edge/Application/msedge.exe",Path(os.environ.get("PROGRAMFILES",r"C:\Program Files"))/"Microsoft/Edge/Application/msedge.exe",Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")]
    return next((p for p in candidates if p.exists()),None)

def pdf_pages(path):
    raw=path.read_bytes()
    return len(re.findall(rb"/Type\s*/Page\b",raw))

def print_pdf(edge,html_path,pdf_path,profile):
    profile.mkdir(parents=True,exist_ok=True)
    cmd=[str(edge),"--headless=new","--disable-gpu","--no-first-run","--no-pdf-header-footer",f"--user-data-dir={profile}",f"--print-to-pdf={pdf_path}",html_path.as_uri()]
    result=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120)
    if result.returncode or not pdf_path.exists(): raise RuntimeError("Edge no generó PDF: "+result.stderr.decode("utf-8",errors="replace")[-1200:])
    pages=pdf_pages(pdf_path)
    if pages<1: raise RuntimeError("No se pudo determinar el número de páginas del PDF")
    return pages

def verify_pdf(pdf_path,title,part,allow_pending=False):
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError as exc:
        raise RuntimeError("Se requiere pypdf para validar texto seleccionable y metadatos del PDF") from exc
    reader=PdfReader(str(pdf_path)); pages=len(reader.pages); content="\n".join(page.extract_text() or "" for page in reader.pages)
    if not content.strip(): raise RuntimeError(f"PDF sin texto seleccionable: {pdf_path.name}")
    if not allow_pending and re.search(r"\bTODO\b|\[VERIFICAR\]",content,re.I): raise RuntimeError(f"PDF contiene marcador pendiente: {pdf_path.name}")
    writer=PdfWriter(); writer.append_pages_from_reader(reader)
    writer.add_metadata({"/Title":title,"/Author":"Only Simple Solutions","/Subject":f"Licitación TFEP-01/2026 · {part}","/Keywords":f"{part}, propuesta técnica, PUCV","/Creator":"Sistema de artefactos verificables"})
    temporary=pdf_path.with_name(pdf_path.stem+".metadata.tmp.pdf")
    with temporary.open("wb") as stream: writer.write(stream)
    temporary.replace(pdf_path)
    raw=pdf_path.read_bytes()
    if not any(marker in raw for marker in (b"/FontFile",b"/FontFile2",b"/FontFile3")):
        raise RuntimeError(f"No se confirmó que el PDF incruste fuentes: {pdf_path.name}")
    return pages

def declared_attachments(fm):
    path=ROOT/"05_Gestion"/"adjuntos.json"
    registry=json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    wanted=set(fm.get("adjuntos",[]))
    return [x for x in registry if x.get("id") in wanted]

def ai_declaration(part,fm,sections,builddir):
    registry_path=ROOT/"05_Gestion"/"ia"/"registro.json"
    registry=json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.exists() else {"registros":[]}
    records={r.get("artefacto"):r for r in registry.get("registros",[])}
    expected=[(sfm.get("id"),section_title) for _,section_title,_,sfm,_ in sections]
    expected += [(r["id"],r["nombre"]) for r in declared_attachments(fm)]
    missing=[aid for aid,_ in expected if aid not in records]
    if missing: raise ValueError("Registro de uso de IA incompleto para: "+", ".join(str(x) for x in missing))
    valid={"Ninguno","Bajo","Medio","Alto"}
    rows=[]
    for aid,title in expected:
        r=records[aid]
        if r.get("nivel_texto") not in valid or r.get("nivel_diagramas") not in valid or not r.get("herramienta") or not r.get("finalidad") or not r.get("verificador") or r.get("verificador"," ").casefold() in {"pendiente","por definir","tbd"} or not r.get("comprobaciones"):
            raise ValueError(f"Registro IA incompleto o inválido: {aid}")
        rows.append((aid,r["herramienta"],r["finalidad"],r["nivel_texto"],r["nivel_diagramas"],r["verificador"]+": "+"; ".join(r["comprobaciones"])))
    body=["# Declaración de uso de IA","","La siguiente declaración identifica el apoyo utilizado en cada artefacto y la verificación humana registrada.","","| Artefacto | Herramienta | Finalidad | Texto | Diagramas | Verificación humana |","|---|---|---|---|---|---|"]
    body += ["| "+" | ".join(str(x).replace("|","\\|").replace("\n"," ") for x in row)+" |" for row in rows]
    path=builddir/f"{part}.declaracion-ia.md"; path.parent.mkdir(parents=True,exist_ok=True); path.write_text("\n".join(body)+"\n",encoding="utf-8")
    fm={"id":part+"-IA","estado":"revisado" if rows else "borrador"}
    return (len(sections)+2,"Declaración de uso de IA",path,fm,"\n".join(body)+"\n")

def annex_html(part,title,record,theme,output,draft):
    source=ROOT/record["ruta"]
    if source.suffix.casefold()==".md":
        annex_meta,body=parse_frontmatter(source.read_text(encoding="utf-8-sig")); title=str(annex_meta.get("titulo",title)); content=fallback_markdown(body)
        def local_uri(match):
            href=match.group(2)
            if href.startswith(("http:","https:","#","data:")): return match.group(0)
            resolved=(source.parent/href).resolve()
            return f'{match.group(1)}="{html.escape(resolved.as_uri(),quote=True)}"'
        content=re.sub(r'(src|href)="([^"]+)"',local_uri,content)
    elif source.suffix.casefold() in {".svg",".png",".jpg",".jpeg",".webp"}:
        content=f'<figure><img src="{html.escape(source.resolve().as_uri(),quote=True)}" alt="{html.escape(source.stem)}"></figure>'
    else: raise ValueError(f"Adjunto {record['id']} requiere conversión no soportada: {source.suffix}")
    css=corporate_css(theme,part,title)
    watermark='<div class="draft-watermark">BORRADOR</div>' if draft else ''
    doc=f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{css}</style></head><body><div class="running-company">{html.escape(str(theme.get("marca","Only Simple Solutions")))}</div>{watermark}<section class="annex-cover"><p class="cover-mark">{html.escape(str(theme.get("marca","Only Simple Solutions")))}</p><h1>{html.escape(title)}</h1><p>{part} · Anexo {html.escape(record["id"])}</p></section><section class="section-content">{content}</section></body></html>'
    output.write_text(doc,encoding="utf-8")
    return title

def export_annexes(part,fm,title,theme,edge,builddir,profile,outdir,draft):
    records=declared_attachments(fm)
    annexes=[r for r in records if not Path(r["nombre"]).name.casefold().startswith("form-")]
    missing=[r["ruta"] for r in annexes if not (ROOT/r["ruta"]).is_file()]
    if missing: raise ValueError("Anexos declarados pendientes: "+", ".join(missing))
    outputs=[]
    for record in annexes:
        source=ROOT/record["ruta"]; label=re.sub(r"[^A-Za-z0-9-]+","-",source.stem).strip("-")
        html_path=builddir/f"{part}.{record['id']}.html"; pdf=outdir/f"OnlySimpleSolutions-Subdocumento{int(part[3:])}-Anexos-{record['id']}_{label}.pdf"
        annex_title=annex_html(part,title+" · "+source.stem,record,theme,html_path,draft)
        pages=print_pdf(edge,html_path,pdf,profile)
        verify_pdf(pdf,annex_title,part)
        if not 1<=pages<=200: raise ValueError(f"Número de páginas fuera de rango en {pdf.name}: {pages}")
        html_path.unlink(missing_ok=True); outputs.append((pdf,pages))
    return outputs

def build_one(part,dry,preview=False):
    folder,master,fm,sections=load_part(part); theme=simple_yaml(THEME)
    title=str(fm.get("titulo",master.stem)); draft=preview or any(sfm.get("estado") not in {"revisado","congelado"} for *_,sfm,body in sections)
    outdir=(ROOT/"05_Gestion"/"reportes"/"vistas_previas") if preview else (ROOT/"07_Entregables"/"sobre_2_tecnico")
    filename=f"{part}_Informes4_preview.pdf" if preview else f"OnlySimpleSolutions-Subdocumento{int(part[3:])}.pdf"; pdf=outdir/filename
    html_path=ROOT/"05_Gestion"/"build"/((part+".preview.html") if preview else (part+".html"))
    if dry:
        print(f"{part}: {len(sections)} secciones, borrador={'sí' if draft else 'no'}, salida={pdf.relative_to(ROOT)}")
        for _,_,p,*_ in sections: print("  "+str(p.relative_to(ROOT)))
        for record in declared_attachments(fm):
            state="pendiente" if not (ROOT/record["ruta"]).exists() else "presente"
            kind="formulario separado" if Path(record["nombre"]).name.casefold().startswith("form-") else "PDF de anexo"
            print(f"  {record['id']} · {kind} · {state}: {record['ruta']}")
        references=folder/f"sd-{int(part[3:]):02d}_referencias.md"
        print(f"  T7-{int(part[3:]):02d}-REF · {'presente' if references.exists() else 'pendiente'}: {references.relative_to(ROOT)}")
        print(f"  T7-{int(part[3:]):02d}-IA · requiere registro humano por sección/anexo/formulario")
        return 0
    for _,_,p,_,body in sections:
        if not preview and re.search(r"\bTODO\b|\[VERIFICAR\]",body,re.I): raise ValueError(f"Marcador pendiente en {p.relative_to(ROOT)}")
        if re.search(r"\bstyle\s*=",body,re.I): raise ValueError(f"Estilo inline prohibido en {p.relative_to(ROOT)}")
    html_path.parent.mkdir(parents=True,exist_ok=True); outdir.mkdir(parents=True,exist_ok=True)
    edge=edge_renderer()
    if not edge: raise RuntimeError("No hay Edge/Chrome disponible para PDF")
    builddir=html_path.parent; profile=builddir/"edge-profile"; front_html=builddir/(part+".front.html"); front_pdf=builddir/(part+".front.pdf")
    annex_records=[] if preview else [r for r in declared_attachments(fm) if not Path(r["nombre"]).name.casefold().startswith("form-")]
    missing_annexes=[r["ruta"] for r in annex_records if not (ROOT/r["ruta"]).is_file()]
    if missing_annexes: raise ValueError("Anexos declarados pendientes: "+", ".join(missing_annexes))
    unsupported=[r["ruta"] for r in annex_records if Path(r["ruta"]).suffix.casefold() not in {".md",".svg",".png",".jpg",".jpeg",".webp"}]
    if unsupported: raise ValueError("Formato de anexo sin conversión implementada: "+", ".join(unsupported))
    if preview:
        output_sections=sections
    else:
        references_path=folder/f"sd-{int(part[3:]):02d}_referencias.md"
        if not references_path.is_file(): raise ValueError(f"Falta la sección final obligatoria Referencias: {references_path.relative_to(ROOT)}")
        references_fm,references_body=parse_frontmatter(references_path.read_text(encoding="utf-8-sig"))
        if not references_body.strip(): raise ValueError("La sección obligatoria Referencias no puede estar vacía")
        if not references_fm.get("id") or references_fm.get("estado") not in {"revisado","congelado"}:
            raise ValueError("Referencias requiere frontmatter con ID y estado revisado/congelado antes de exportar")
        if re.search(r"\bTODO\b|\[VERIFICAR\]",references_body,re.I) or re.search(r"\bstyle\s*=",references_body,re.I):
            raise ValueError("Referencias contiene un marcador pendiente o estilos inline prohibidos")
        ref_tuple=(len(sections)+1,"Referencias",references_path,references_fm,references_body)
        ia_tuple=ai_declaration(part,fm,sections,builddir)
        output_sections=sections+[ref_tuple,ia_tuple]
        draft=draft or references_fm.get("estado") not in {"revisado","congelado"}
    render_html(part,title,output_sections,theme,draft,front_html,front_only=True)
    fixed_pages=print_pdf(edge,front_html,front_pdf,profile)
    page_map={}; page_cursor=fixed_pages+1; section_pdfs=[]
    for i,section in enumerate(output_sections):
        section_html=builddir/f"{part}.section-{i+1}.html"; section_pdf=builddir/f"{part}.section-{i+1}.pdf"
        render_html(part,title,output_sections,theme,draft,section_html,section_only=i)
        section_pages=print_pdf(edge,section_html,section_pdf,profile); page_map[f"seccion-{i+1}"]=page_cursor
        page_cursor+=section_pages; section_pdfs.append(section_pdf)
    render_html(part,title,output_sections,theme,draft,html_path,page_numbers=None if preview else page_map)
    expected_pages=page_cursor-1; pages=print_pdf(edge,html_path,pdf,profile)
    front_html.unlink(missing_ok=True); front_pdf.unlink(missing_ok=True)
    for p in section_pdfs: p.unlink(missing_ok=True)
    for p in builddir.glob(f"{part}.section-*.html"): p.unlink(missing_ok=True)
    if pages!=expected_pages and not preview: raise RuntimeError(f"Paginación cambió tras insertar números del índice: esperado {expected_pages}, obtenido {pages}")
    if pages<1 or pages>200: raise RuntimeError(f"Número de páginas fuera del rango permitido (1-200): {pages}")
    verify_pdf(pdf,title,part,allow_pending=preview)
    print(f"PDF generado: {pdf.relative_to(ROOT)} ({pages} páginas; {'BORRADOR' if draft else 'revisado'})")
    if not preview:
        for annex_pdf,annex_pages in export_annexes(part,fm,title,theme,edge,builddir,profile,outdir,draft):
            print(f"Anexo PDF: {annex_pdf.relative_to(ROOT)} ({annex_pages} páginas)")
        print(f"HTML derivado disponible para importar como Google Docs: {html_path.relative_to(ROOT)}")
    else:
        print(f"Vista previa BORRADOR: {pdf.relative_to(ROOT)} ({pages} páginas); no es un entregable final")
    return 0

def main():
    ap=argparse.ArgumentParser(description=__doc__); group=ap.add_mutually_exclusive_group(required=True); group.add_argument("--parte"); group.add_argument("--todo",action="store_true"); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--muestra",action="store_true",help="Renderiza plantillas/muestra.md en staging para QA visual"); ap.add_argument("--vista-previa",action="store_true",help="Genera un PDF de borrador aislado en reportes, sin referencias ni declaración final de IA")
    a=ap.parse_args(); parts=[a.parte] if a.parte else [f"T7-{i:02d}" for i in range(1,15)]
    try:
        if a.muestra:
            theme=simple_yaml(THEME); out=ROOT/"05_Gestion"/"build"/"muestra.html"; out.parent.mkdir(parents=True,exist_ok=True)
            render_html("T7-00","Muestra visual",[(1,"Componentes",ROOT/"plantillas"/"muestra.md",{},(ROOT/"plantillas"/"muestra.md").read_text(encoding="utf-8"))],theme,True,out,page_numbers={"seccion-1":3})
            print(f"Muestra HTML creada: {out.relative_to(ROOT)}")
            if not a.dry_run:
                edge=edge_renderer()
                if not edge: raise RuntimeError("No hay Edge/Chrome disponible para PDF")
                pdf=ROOT/"05_Gestion"/"reportes"/"muestra_visual.pdf"; pdf.parent.mkdir(parents=True,exist_ok=True)
                subprocess.run([str(edge),"--headless=new","--disable-gpu","--no-pdf-header-footer",f"--user-data-dir={ROOT/'05_Gestion'/'build'/'edge-profile-sample'}",f"--print-to-pdf={pdf}",out.as_uri()],check=True,timeout=120)
                verify_pdf(pdf,"Muestra visual","T7-00")
                print(f"Muestra PDF: {pdf.relative_to(ROOT)}")
            return 0
        if a.vista_previa and a.todo: raise ValueError("--vista-previa requiere --parte; no se ejecuta sobre todas las partes")
        code=0
        for part in parts:
            try: code=max(code,build_one(part,a.dry_run,preview=a.vista_previa))
            except Exception as exc: print(f"{part}: {exc}",file=sys.stderr); code=1
        return code
    except Exception as exc: print(f"Error: {exc}",file=sys.stderr); return 1

if __name__=="__main__": raise SystemExit(main())
