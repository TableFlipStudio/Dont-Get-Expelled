@echo off

python -m pip install pygame 
python -m pip install pytmx 

cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

move bat-files\RUN-Dont-Get-Expelled.bat %USERPROFILE%\Desktop\DoGeX

cd /d %USERPROFILE%\Desktop\DoGeX

start RUN-Dont-Get-Expelled.bat && del /Q %USERPROFILE%\Desktop\DoGeX\START-Dont-Get-Expelled.bat