@echo off

del /Q %USERPROFILE%\Desktop\DOWNLOAD_LIBS.bat

cd %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

python dontgetexpelled.py
