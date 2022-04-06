@echo off

set /A i=0
python --version || set /A i=1


if %i%==1 (

		
		echo. 
		echo WAIT PATIENTLY! 
		echo.  
		
		curl https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe -o %USERPROFILE%\Downloads\python-3.10.4-amd64.exe
		
		echo. 
		
		cd %USERPROFILE%\Downloads/
		
		
		python-3.10.4-amd64.exe /quiet PrependPath=1
)

mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\

curl -L https://github.com/TabeFlipStudio/Dont-Get-Expelled/archive/refs/heads/main.zip -o %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip

powershell expand-archive %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip %USERPROFILE%\Documents\Dont-Get-Expelled\

cd %USERPROFILE%\Documents\Dont-Get-Expelled

del /Q Dont-Get-Expelled.zip

ren Dont-Get-Expelled-main Dont-Get-Expelled

move Dont-Get-Expelled\gamefiles %USERPROFILE%\Documents\Dont-Get-Expelled\

move gamefiles\START-Dont-Get-Expelled-The-Batory-game.bat %USERPROFILE%\Desktop\

rmdir Dont-Get-Expelled

cls

echo The program is now installed, RESTART the system and open the START-Dont-Get-Expelled-The-Batory-game.bat file
pause
