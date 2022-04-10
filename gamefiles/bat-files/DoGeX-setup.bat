@echo off
set /A installed=0

mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\ || set /A installed=1

set /A python=0
python --version || set /A python=1
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
echo.

if %python%==1 (

    echo Python is not installed!
		echo.
		echo Installing Python...
		echo.
		cls
		echo Now there will be a window with a shield open, select yes.
		echo.
		pause 
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

cd /d %USERPROFILE%\Desktop

cd /d %USERPROFILE%\Documents\Dont-Get-Expelled

del /Q /F Dont-Get-Expelled.zip

move Dont-Get-Expelled-main\gamefiles %USERPROFILE%\Documents\Dont-Get-Expelled\

move gamefiles\bat-files\START-DoGeX.bat %USERPROFILE%\Desktop\

move gamefiles\bat-files\uninstall-DoGeX.bat %USERPROFILE%\Documents\Dont-Get-Expelled\

move gamefiles\bat-files\Game-Manual.bat %USERPROFILE%\Documents\Dont-Get-Expelled\

del /Q %USERPROFILE%\Downloads\python-3.10.4-amd64.exe

mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\temporary

rmdir /Q /s Dont-Get-Expelled-main

cls

echo The program is now installed, RESTART the system and open the START-Dont-Get-Expelled.bat file
pause

del /Q /F %USERPROFILE%\Downloads\DoGeX-setup.bat
