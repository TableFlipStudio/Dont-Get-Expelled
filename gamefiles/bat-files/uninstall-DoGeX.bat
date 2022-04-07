@echo off 

echo This program is going to uninstall the game!!
pause

del /Q %USERPROFILE%\Documents\Dont-Get-Expelled\

rmdir /q /s %USERPROFILE%\Documents\Dont-Get-Expelled

echo The game has been uninstalled.

del /Q %USERPROFILE%\Desktop\RUN-Dont-Get-Expelled-The-Batory-game.bat

pause
del /Q %USERPROFILE%\Desktop\uninstall-DoGeX.bat