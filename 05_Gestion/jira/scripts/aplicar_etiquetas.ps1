$ErrorActionPreference = 'Stop'
# Rutas resueltas desde la ubicacion del script: funciona desde cualquier directorio.
$jira   = Split-Path -Parent $PSScriptRoot
$mapa   = Join-Path $jira 'mapeo\restructuracion_2026-09-29_etiquetas.json'
$auth   = Join-Path $env:USERPROFILE '.local\share\opencode\mcp-auth.json'
$tok    = (Get-Content -LiteralPath $auth -Raw | ConvertFrom-Json).jira.tokens.accessToken
$base   = 'https://api.atlassian.com/ex/jira/b662438c-9aba-4643-a083-82a2fde025f3/rest/api/3'
$mapaJson = Get-Content -LiteralPath $mapa -Raw | ConvertFrom-Json

$ok = 0
$fail = 0
foreach ($prop in $mapaJson.PSObject.Properties) {
    $key = $prop.Name
    $labels = @($prop.Value)
    $body = @{ fields = @{ labels = $labels } } | ConvertTo-Json -Depth 5 -Compress
    $tmp = Join-Path $env:TEMP "labels_$key.json"
    [System.IO.File]::WriteAllText($tmp, $body, (New-Object System.Text.UTF8Encoding($false)))
    $code = curl.exe -s -o NUL -w "%{http_code}" -X PUT -H "Authorization: Bearer $tok" -H "Content-Type: application/json" --data-binary "@$tmp" "$base/issue/$key"
    Remove-Item -LiteralPath $tmp -ErrorAction SilentlyContinue
    if ($code -eq '204') { $ok++ } else { $fail++; Write-Output "FALLO $key -> $code" }
}
Write-Output "aplicadas=$ok fallos=$fail"
