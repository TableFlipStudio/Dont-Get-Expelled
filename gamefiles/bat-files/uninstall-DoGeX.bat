@echo off 

echo This program is going to uninstall the game!!
pause

del /Q %USERPROFILE%\Documents\Dont-Get-Expelled\

rmdir /q /s %USERPROFILE%\Documents\Dont-Get-Expelled

del /Q %USERPROFILE%\Desktop\RUN-Dont-Get-Expelled.bat

echo The game has been uninstalled.

pause
del /Q %USERPROFILE%\Desktop\uninstall-DoGeX.bat