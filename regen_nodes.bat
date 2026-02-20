@echo off
setlocal

echo ------------------------------------------
echo Regen Atom 2.1 generated artifacts
echo ------------------------------------------
echo.
echo This will regenerate:
echo   - nodes/*/claims.md
echo   - NODE_INDEX.md
echo   - TREE.dot
echo   - papers/P001_foundations/outline.md
echo.

python scripts\build_node_claims.py
if errorlevel 1 goto :err

python scripts\build_node_index.py
if errorlevel 1 goto :err

python scripts\build_paper_outline.py
if errorlevel 1 goto :err

echo.
echo DONE: regenerated artifacts.
echo.
echo Next (manual):
echo   git add -A
echo   git commit -m "Regenerate artifacts"
echo   git push
echo.
goto :eof

:err
echo.
echo ERROR: regeneration failed.
echo Fix the error above, then rerun regen_nodes.bat
echo.
exit /b 1
