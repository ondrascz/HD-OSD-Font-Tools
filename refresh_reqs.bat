@echo off

echo Rerfreshing requirements.txt
echo !!! Make sure the .venv is activated !!!

pause

pip freeze > requirements.txt

pause