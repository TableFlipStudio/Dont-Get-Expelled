@echo off

echo This program is going to uninstall the game!!
echo.
pause

::go to the desktop
cd /d %USERPROFILE%\Desktop

::if the uninstall game file is ran before running the game for the first time:
::delete the starter file
del /Q %USERPROFILE%\Desktop\STARTER-DoGeX.bat

:: and delete the start file
del /Q %USERPROFILE%\Desktop\START-DoGeX.bat

cls

echo.
echo The game has been uninstalled.
echo.
pause

::go to the game folder 
cd /d %USERPROFILE%\Documents\

::delete the game files all together
rmdir /Q /s Dont-Get-Expelled

