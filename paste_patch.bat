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

python agent_apply.py --stdin

echo.
echo ------------------------------------------
echo Done (or exited). Press any key to close.
echo ------------------------------------------
pause >nul
endlocal