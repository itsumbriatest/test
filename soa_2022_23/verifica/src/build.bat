@ECHO OFF
pyinstaller -y -w --onefile -n verifica --uac-admin --clean verifica.py
REM pyinstaller -y -w --onefile -n verifica --clean verifica.py