-- Pandoc Lua filter: normaliza solo componentes corporativos declarados.
local allowed = { ["callout-info"] = true, ["callout-alerta"] = true,
  ["kpi"] = true, ["resumen-ejecutivo"] = true,
  ["estado-completado"] = true }

function Div(el)
  local kept = {}
  for _, class in ipairs(el.classes) do
    if allowed[class] then kept[#kept + 1] = class end
  end
  el.classes = kept
  return el
end

function Table(el)
  el.attr.classes:insert("tabla-corporativa")
  return el
end
