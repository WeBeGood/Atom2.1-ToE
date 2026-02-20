@echo off
setlocal
cd /d "%~dp0"

if not exist LLM_WORKSPACE_INIT.txt (
  echo ERROR: LLM_WORKSPACE_INIT.txt not found in this folder.
  pause
  exit /b 1
)

if not exist Atom2.1_superseed.yaml (
  echo ERROR: Atom2.1_superseed.yaml not found in this folder.
  pause
  exit /b 1
)

(
  type LLM_WORKSPACE_INIT.txt
  echo.
  echo ==========================================
  echo NEXT: PASTE Atom2.1_superseed.yaml BELOW
  echo ==========================================
  echo.
  type Atom2.1_superseed.yaml
) | clip

echo Bootstrap text (INIT + SuperSeed) copied to clipboard.
echo Paste into any LLM chat (Ctrl+V).
pause
endlocal