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
  echo.
  echo ==========================================
  echo CONFIRM LOADED (ask the model to reply)
  echo ==========================================
  echo Confirm you loaded Atom2.1_superseed.yaml. Return:
  echo A) LOADED: yes/no
  echo B) NEXT_FOCUS (bullets)
  echo C) OPEN_ISSUES_TOP3 (bullets)
  echo D) FIRST_ACTION (one step)
  echo.
  echo ==========================================
  echo END OF SESSION (how to push changes)
  echo ==========================================
  echo When ready to commit changes, say: MAKE PATCH
  echo Then on Windows: double-click paste_patch.bat
  echo Paste the JSON, press Enter, then Ctrl+Z, then Enter.
) | clip

echo Bootstrap text (INIT + SuperSeed) copied to clipboard.
echo Paste into any LLM chat (Ctrl+V).
pause
endlocal