@echo off

echo This program is going to uninstall the game!!
pause

del /Q /F %USERPROFILE%\Documents\Dont-Get-Expelled\

rmdir /Q /S %USERPROFILE%\Documents\Dont-Get-Expelled

del /Q /F %USERPROFILE%\Desktop\START-Dont-Get-Expelled.bat

del /Q /F %USERPROFILE%\Desktop\RUN-Dont-Get-Expelled.bat

echo The game has been uninstalled.

pause

rmdir /Q /S %USERPROFILE%\Desktop\DoGeX\
