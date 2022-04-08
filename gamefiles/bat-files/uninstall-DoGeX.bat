@echo off

echo This program is going to uninstall the game!!
pause

cd /d %USERPROFILE%\Documents\

rmdir /Q /s Dont-Get-Expelled

cd /d %USERPROFILE%\Desktop

echo The game has been uninstalled.

pause

rmdir /Q /s %USERPROFILE%\Desktop\DoGeX

