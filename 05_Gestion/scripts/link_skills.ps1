param([switch]$DryRun)
# Envoltorio: la lógica multiplataforma vive en link_skills.py (junctions en Windows).
$script = Join-Path $PSScriptRoot 'link_skills.py'
$py = if (Get-Command python -ErrorAction SilentlyContinue) { 'python' } else { 'py' }
if ($DryRun) { & $py $script --dry-run } else { & $py $script }
exit $LASTEXITCODE
