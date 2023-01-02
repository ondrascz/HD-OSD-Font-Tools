@echo off

echo Creating .venv Python virtual environment
py -3 -m venv .venv

echo Activating .venv Python virtual environment
call .venv\scripts\activate

echo Installing the requirements
pip install -r requirements.txt

pause