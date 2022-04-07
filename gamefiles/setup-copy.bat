@echo off

cls #clear the screen

set /A i=0
python --version || set /A i=1
cls
echo.

echo Welcome to the setup script for the DontGetExpelled setup
echo This script will install Python 3.10.2, the required libraries for the setup, and the main program

echo.
pause

cls

echo Checking if python is installed and/or Downloading Python 3.10.2
echo.


if %i%==1 (

		echo Python is not installed.
		echo.
		echo installing Python...
		echo.
		echo WAIT PATIENTLY!
		echo.

		curl https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe -o %USERPROFILE%\Downloads\python-3.10.4-amd64.exe

		echo.

		echo Now there will be a window with a shield open, check the yes box and press Enter, OK?
		echo.

		pause

		cd %USERPROFILE%\Downloads/
		echo Installing Python 3.10.2
		echo.

		python-3.10.4-amd64.exe /quiet PrependPath=1
)

echo Python is installed!
echo.

cls

echo Now, there will be the main file downloaded, WAIT until it is done, OK?
pause
echo.
echo downloading the game files...

mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\

curl -L https://github.com/TabeFlipStudio/Dont-Get-Expelled/archive/refs/heads/main.zip -o %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip

powershell expand-archive %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip %USERPROFILE%\Documents\Dont-Get-Expelled\

cd %USERPROFILE%\Documents\Dont-Get-Expelled

del /Q Dont-Get-Expelled.zip

ren Dont-Get-Expelled-main Dont-Get-Expelled

move Dont-Get-Expelled\gamefiles %USERPROFILE%\Documents\Dont-Get-Expelled\

move gamefiles\DOWNLOAD_LIBS.bat %USERPROFILE%\Desktop\

rmdir Dont-Get-Expelled

cls

echo The program is now installed, RESTART the system and open the DOWNLOAD_LIBS.bat file
pause
