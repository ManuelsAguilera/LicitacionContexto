param([switch]$DryRun)
$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$names = @('redactar-seccion', 'revisar-seccion', 'cerrar-parte', 'exportar')
foreach ($name in $names) {
    $target = Join-Path $repo ('.agents\skills\' + $name)
    foreach ($parent in @('.claude\skills', '.opencode\skills')) {
        $link = Join-Path $repo (Join-Path $parent $name)
        if (Test-Path -LiteralPath $link) {
            $item = Get-Item -LiteralPath $link -Force
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { continue }
            if (@(Get-ChildItem -LiteralPath $link -Force).Count -gt 0) { throw "No se reemplaza una carpeta no vacía: $link" }
            if (-not $DryRun) { Remove-Item -LiteralPath $link }
        }
        if ($DryRun) { Write-Output "Junction: $link -> $target" }
        else {
            $command = 'mklink /J "' + $link + '" "' + $target + '"'
            & cmd.exe /c $command | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "No se pudo crear junction: $link" }
        }
    }
}
