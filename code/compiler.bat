@echo off

where python >nul 2>nul
if %errorlevel%==0 (
    python -m pip install --upgrade pip

    python -m pip install pyinstaller

    python -m pip install -r requirements.txt

    pyinstaller --onefile --name FMaVM.exe main.py
) else (
    echo install python3
)
