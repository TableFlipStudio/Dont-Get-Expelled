@echo off

python -m pip install pygame
python -m pip install pytmx

cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

move bat-files\START-DoGeX.bat %USERPROFILE%\Desktop

echo.
echo The STARTER-DoGeX file was replaced by a START-DoGeX file on your Desktop
echo.
pause

cd /d %USERPROFILE%\Desktop

start START-DoGeX.bat & del /Q %USERPROFILE%\Desktop\STARTER-DoGeX.bat & exit /B

