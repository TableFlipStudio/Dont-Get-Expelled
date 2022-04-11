@echo off

python -m pip install pygame
python -m pip install pytmx

cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

move bat-files\RUN-DoGeX.bat %USERPROFILE%\Desktop

echo.
echo The START-DoGeX file was replaced by a RUN-DoGeX file on your Desktop
echo.
pause

cd /d %USERPROFILE%\Desktop

start RUN-DoGeX.bat & del /Q %USERPROFILE%\Desktop\START-DoGeX.bat & exit /B

