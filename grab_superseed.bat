@echo off
setlocal
cd /d "%~dp0"

if not exist Atom2.1_superseed.yaml (
  echo ERROR: Atom2.1_superseed.yaml not found in this folder.
  pause
  exit /b 1
)

type Atom2.1_superseed.yaml | clip
echo Atom2.1_superseed.yaml copied to clipboard.
echo Now paste into your LLM chat (Ctrl+V).
pause
endlocal