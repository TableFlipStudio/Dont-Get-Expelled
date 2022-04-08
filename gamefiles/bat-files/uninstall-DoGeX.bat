@echo off 

echo This program is going to uninstall the game!!
pause

del /Q %USERPROFILE%\Documents\Dont-Get-Expelled\

rmdir /Q %USERPROFILE%\Documents\Dont-Get-Expelled

del /Q %USERPROFILE%\Desktop\START-Dont-Get-Expelled.bat

del /Q %USERPROFILE%\Desktop\RUN-Dont-Get-Expelled.bat

echo The game has been uninstalled.

pause

rmdir /Q %USERPROFILE%\Desktop\DoGeX\
