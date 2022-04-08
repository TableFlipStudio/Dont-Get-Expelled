@echo off

python -m pip install pygame
python -m pip install pytmx

cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

move bat-files\RUN-DoGeX.bat %USERPROFILE%\Desktop

cd /d %USERPROFILE%\Desktop

start RUN-DoGeX.bat & del /Q %USERPROFILE%\Desktop\START-DoGeX.bat & exit /B

