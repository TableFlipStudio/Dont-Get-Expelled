@echo off

python -m pip install pygame
python -m pip install pytmx

cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

move bat-files\RUN-Dont-Get-Expelled.bat %USERPROFILE%\Desktop\Dont-Get-Expelled

cd /d %USERPROFILE%\Desktop\Dont-Get-Expelled

start RUN-DoGeX.bat && del /Q %USERPROFILE%\Desktop\Dont-Get-Expelled\START-DoGeX.bat

exit

