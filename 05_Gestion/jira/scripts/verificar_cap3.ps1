$ErrorActionPreference = 'Stop'
$auth = Join-Path $env:USERPROFILE '.local\share\opencode\mcp-auth.json'
$tok = (Get-Content -LiteralPath $auth -Raw | ConvertFrom-Json).jira.tokens.accessToken
$h = @{ Authorization = "Bearer $tok"; Accept = 'application/json' }
$base = 'https://api.atlassian.com/ex/jira/b662438c-9aba-4643-a083-82a2fde025f3/rest/api/3'

# --- Trae todas las incidencias del proyecto (endpoint nuevo /search/jql) ---
$todas = @()
$token = $null
do {
    $u = $base + '/search/jql?jql=' + [uri]::EscapeDataString('project = OSS ORDER BY key ASC') +
         '&fields=key,parent,labels,summary,assignee&maxResults=100'
    if ($token) { $u += '&nextPageToken=' + [uri]::EscapeDataString($token) }
    $r = Invoke-RestMethod -Uri $u -Headers $h
    $todas += $r.issues
    $token = $r.nextPageToken
} while ($token)

Write-Output ("Incidencias en el proyecto: {0}" -f $todas.Count)

function Num([string]$k) { [int]($k -replace '^OSS-', '') }

$hijas    = $todas | Where-Object { $_.fields.parent }
$topes    = $todas | Where-Object { -not $_.fields.parent }
$etiquet  = $todas | Where-Object { $_.fields.labels.Count -gt 0 }

Write-Output ("  sin padre        : {0}" -f $topes.Count)
Write-Output ("  con padre        : {0}" -f $hijas.Count)
Write-Output ("  con etiquetas    : {0}" -f $etiquet.Count)

$agrupadoras = 165..172 | ForEach-Object { "OSS-$_" }
$enAgrup = @($todas | Where-Object { $agrupadoras -contains $_.key })
Write-Output ("  hijas de agrupadoras OSS-165..172 : {0}" -f @($todas | Where-Object { $_.fields.parent -and $agrupadoras -contains $_.fields.parent.key }).Count)
Write-Output ("  hijas de historias (subtareas)    : {0}" -f @($todas | Where-Object { $_.fields.parent -and $agrupadoras -notcontains $_.fields.parent.key }).Count)

Write-Output ""
Write-Output "=== CAP 3: subtareas por Historia ==="
foreach ($k in @('OSS-84','OSS-85','OSS-86','OSS-87','OSS-88')) {
    $n = @($todas | Where-Object { $_.fields.parent -and $_.fields.parent.key -eq $k }).Count
    Write-Output ("{0} : {1} subtareas" -f $k, $n)
}

Write-Output ""
Write-Output "=== LAS 14 NUEVAS DEL CAP 3 ==="
$topes | Out-Null
foreach ($k in 236..249) {
    $key = "OSS-$k"
    $i = $todas | Where-Object { $_.key -eq $key }
    if (-not $i) { Write-Output ("{0}  NO ENCONTRADA" -f $key); continue }
    $p = if ($i.fields.parent) { $i.fields.parent.key } else { 'SIN PADRE' }
    $a = if ($i.fields.assignee) { $i.fields.assignee.displayName } else { '-' }
    Write-Output ("{0}  padre={1}  et={2}  resp={3}  {4}" -f $key, $p, ($i.fields.labels -join '|'), $a, $i.fields.summary)
}

Write-Output ""
Write-Output "=== TOPES SIN PADRE (agrupadoras + originales + OSS-1/2) ==="
$topes | Sort-Object { Num $_.key } | ForEach-Object { Write-Output ("  {0}  {1}" -f $_.key, $_.fields.summary) }

Write-Output ""
Write-Output "=== ENLACES DE OSS-243 (Validar supuestos) ==="
$iss = Invoke-RestMethod -Uri ($base + '/issue/OSS-243?fields=issuelinks') -Headers $h
$links = @($iss.fields.issuelinks)
Write-Output ("total enlaces: {0}" -f $links.Count)
foreach ($l in $links) {
    if ($l.outwardIssue) {
        Write-Output ("  bloqueada por {0}  [{1}]  {2}" -f $l.outwardIssue.key, $l.type.name, $l.outwardIssue.fields.summary)
    } elseif ($l.inwardIssue) {
        Write-Output ("  bloquea a     {0}  [{1}]  {2}" -f $l.inwardIssue.key, $l.type.name, $l.inwardIssue.fields.summary)
    }
}
