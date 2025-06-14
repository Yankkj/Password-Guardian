@echo off

if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Checking dependencies...
pip install -r requirements.txt || (
    echo Failed to install dependencies. Check requirements.txt.
    pause
    exit /b 1
)

echo Starting Password Guardian...
python -m src.gui

pause