@echo off
chcp 65001 >nul
cd /d "%~dp0"
where python >nul 2>&1
if errorlevel 1 (
    echo Python topilmadi. https://www.python.org/downloads/ dan o'rnating
    echo va o'rnatishda "Add python.exe to PATH" ni belgilang.
    pause
    exit /b 1
)
python setup_run.py
pause
