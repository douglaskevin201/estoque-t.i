@echo off
cd /d "%~dp0"

if not exist "libs" (
    echo Primeira execucao nesta maquina - instalando dependencias...
    pip install -r requirements.txt --target=libs
)

set PYTHONPATH=%~dp0libs
python menu.py
pause