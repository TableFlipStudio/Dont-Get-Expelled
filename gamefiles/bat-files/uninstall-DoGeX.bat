@echo off

echo This program is going to uninstall the game!!
echo.
pause

cd /d %USERPROFILE%\Desktop

del /Q %USERPROFILE%\Desktop\STARTER-DoGeX.bat

del /Q %USERPROFILE%\Desktop\START-DoGeX.bat

cls

echo.
echo The game has been uninstalled.
echo.
pause


cd /d %USERPROFILE%\Documents\

rmdir /Q /s Dont-Get-Expelled

