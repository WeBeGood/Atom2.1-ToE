@echo off
setlocal
cd /d "%~dp0"

if not exist PATCH_SPEC.md (
  echo ERROR: PATCH_SPEC.md not found in this folder.
  echo If you want, create it first (or ask me for a patch bundle to add it).
  pause
  exit /b 1
)

type PATCH_SPEC.md | clip
echo PATCH_SPEC.md copied to clipboard.
echo Paste into your LLM chat (Ctrl+V).
pause
endlocal