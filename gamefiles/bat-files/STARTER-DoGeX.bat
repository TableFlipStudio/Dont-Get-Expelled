@echo off

::download the game libraries
python -m pip install pygame
python -m pip install pytmx

::go back to the main game folder
cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

::move the usual game installer file to the desktop
move bat-files\START-DoGeX.bat %USERPROFILE%\Desktop

echo.
echo The STARTER-DoGeX file was replaced by a START-DoGeX file on your Desktop
echo.
pause

::goto desktop
cd /d %USERPROFILE%\Desktop

::open the START file in a new window and delete the STARTER file
start START-DoGeX.bat & del /Q %USERPROFILE%\Desktop\STARTER-DoGeX.bat & exit /B

