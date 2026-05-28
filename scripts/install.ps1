# Install the Flux Cursor skill by symlinking this repo into ~/.cursor/skills/flux
param(
    [string]$RepoPath = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

$SkillsDir = Join-Path $env:USERPROFILE ".cursor\skills"
$Target = Join-Path $SkillsDir "flux"

New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null

if (Test-Path $Target) {
    $item = Get-Item $Target -Force
    if ($item.LinkType -eq "Junction" -or $item.LinkType -eq "SymbolicLink") {
        Remove-Item $Target -Force
    } else {
        Write-Error "Path already exists and is not a symlink: $Target"
        exit 1
    }
}

cmd /c mklink /J "$Target" "$RepoPath"
Write-Host "Linked $Target -> $RepoPath"
Write-Host "In Cursor chat, mention Flux or ask the agent to use the flux skill."
