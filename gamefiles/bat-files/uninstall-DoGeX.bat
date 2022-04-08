@echo off

echo This program is going to uninstall the game!!
echo.
pause

cd /d %USERPROFILE%\Documents\

rmdir /Q /s Dont-Get-Expelled

cd /d %USERPROFILE%\Desktop

echo.
echo The game has been uninstalled.
echo.
pause

rmdir /Q /s %USERPROFILE%\Desktop\Dont-Get-Expelled

