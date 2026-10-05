-- Filtro común de importación Markdown -> LaTeX corporativo.
-- Lo aplica exclusivamente 05_Gestion/scripts/exportar_latex.py importar.

local function is_br(raw)
  return raw.format == "html" and raw.text:match("^<%s*br%s*/?%s*>$")
end

-- HTML incrustado: <br> se conserva como salto de línea; comentarios y demás HTML se descartan.
function RawInline(el)
  if is_br(el) then
    return pandoc.LineBreak()
  end
  if el.format == "html" then
    return {}
  end
end

function RawBlock(el)
  if el.format == "html" then
    return {}
  end
end

-- Bloques de código: sin resaltado (la plantilla no define Shaded); Mermaid prohibido.
function CodeBlock(el)
  for _, class in ipairs(el.classes) do
    if class:lower() == "mermaid" then
      error("bloque Mermaid no admitido: incrustar la imagen exportada")
    end
  end
  return pandoc.CodeBlock(el.text)
end

-- Niveles de título: el menor nivel del documento pasa a \section y no se permiten saltos.
function Pandoc(doc)
  local min_level = nil
  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" and (min_level == nil or block.level < min_level) then
      min_level = block.level
    end
  end
  if min_level == nil then
    return doc
  end
  local previous = 0
  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" then
      local level = block.level - min_level + 1
      if level > previous + 1 then
        level = previous + 1
      end
      block.level = level
      previous = level
    end
  end
  return doc
end
