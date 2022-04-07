@echo off

python -m pip install pygame 
python -m pip install pytmx 

move %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles\bat-files\RUN-Dont-Get-Expelled.bat %USERPROFILE%\Desktop\

start %USERPROFILE%\Desktop\RUN-Dont-Get-Expelled.bat && del /Q %USERPROFILE%\Desktop\START-Dont-Get-Expelled.bat