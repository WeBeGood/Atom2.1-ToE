@echo off
setlocal
echo.
echo ==========================================
echo  Atom 2.1 Patch Paste Mode
echo ==========================================
echo.
echo Paste your PATCH JSON now.
echo When finished, press Ctrl+Z then Enter.
echo.
echo (Tip: This window will stay open on errors.)
echo.
echo.

python agent_apply.py --stdin

set "COMMIT="
for /f %%i in ('git rev-parse --short HEAD 2^>nul') do set "COMMIT=%%i"

echo.
echo ------------------------------------------
if defined COMMIT (
  echo Last commit: %COMMIT%
) else (
  echo Last commit: (unavailable)
)
echo Press any key to close.
echo ------------------------------------------
pause >nul
endlocal
