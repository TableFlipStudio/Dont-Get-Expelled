@echo off

del /Q %USERPROFILE%\Desktop\START-Dont-Get-Expelled.bat || cls

cd %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

python dontgetexpelled.py
