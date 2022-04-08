@echo off
set /A installed=0

mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\ || set /A installed=1

cls

echo -----------------INSTALLER OF THE GAME------------------
echo -------------------Dont-Get-Expelled--------------------
echo ---------------------Version 0.5.0----------------------
echo.
echo This program is going to install the game aswell as python and other necessary libraries if you dont already have them.
echo.
pause
if %installed%==1 (
		echo.
		echo The game is already installed!
		echo.
		pause
	exit /B
)

echo.
echo initializing the download...

set /A i=0
python --version || set /A i=1


if %i%==1 (

    echo Python is not installed!
		echo.
		echo Installing Python...
		echo.
		echo WAIT PATIENTLY!!!
		echo.

		curl https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe -o %USERPROFILE%\Downloads\python-3.10.4-amd64.exe

		echo.

		cd/d %USERPROFILE%\Downloads/


		python-3.10.4-amd64.exe /quiet PrependPath=1
)
echo Python installed!
echo.
echo Installing and unpacking the main game files...
echo.
curl -L https://github.com/TabeFlipStudio/Dont-Get-Expelled/archive/refs/heads/main.zip -o %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip

powershell expand-archive %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip %USERPROFILE%\Documents\Dont-Get-Expelled\

cd/d/d %USERPROFILE%\Documents\Dont-Get-Expelled

del /Q /F Dont-Get-Expelled.zip

move Dont-Get-Expelled-main\gamefiles %USERPROFILE%\Documents\Dont-Get-Expelled\

mkdir %USERPROFILE%\Desktop\DoGeX

move gamefiles\bat-files\START-Dont-Get-Expelled.bat %USERPROFILE%\Desktop\DoGeX

move gamefiles\bat-files\uninstall-DoGeX.bat %USERPROFILE%\Desktop\DoGeX

del /Q /F Dont-Get-Expelled-main

rmdir Dont-Get-Expelled-main

cls

echo The program is now installed, RESTART the system and open the START-Dont-Get-Expelled.bat file
pause
