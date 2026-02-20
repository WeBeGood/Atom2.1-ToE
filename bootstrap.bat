@echo off
setlocal
echo Running Atom 2.1 validation...
python validate_atom2_1.py
if errorlevel 1 (
  echo.
  echo Validation failed.
  exit /b 1
)
echo.
echo Validation passed.
echo.
echo ===== LLM_BOOTSTRAP_PROMPT.txt =====
type LLM_BOOTSTRAP_PROMPT.txt
echo.
echo ===================================
endlocal