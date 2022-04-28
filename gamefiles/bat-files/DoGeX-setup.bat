@echo off
set /A installed=0

::check if the game is installed
mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\ || set /A installed=1

set /A python=0
::check if python is installed
python --version || set /A python=1
cls

echo -----------------INSTALLER OF THE GAME------------------
echo -------------------Dont-Get-Expelled--------------------
echo ---------------------Version 1.0.0----------------------
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

		::download python
		curl https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe -o %USERPROFILE%\Downloads\python-3.10.4-amd64.exe

		echo.

		::the /g flag means that the system can change the disk when chenging the directory
		cd/d %USERPROFILE%\Downloads/

		::install python
		python-3.10.4-amd64.exe /quiet PrependPath=1
)
echo Python installed!
echo.
echo Installing and unpacking the main game files...
echo.
::download the game files
curl -L https://github.com/TabeFlipStudio/Dont-Get-Expelled/archive/refs/heads/main.zip -o %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip

::unpack the game files
powershell expand-archive %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip %USERPROFILE%\Documents\Dont-Get-Expelled\

::go to the game folder
cd /d %USERPROFILE%\Documents\Dont-Get-Expelled 

::delete the zip file
del /Q /F Dont-Get-Expelled.zip 

::move the game files to the game folder
move Dont-Get-Expelled-main\gamefiles %USERPROFILE%\Documents\Dont-Get-Expelled\ 

::move the starter file to the desktop
move gamefiles\bat-files\STARTER-DoGeX.bat %USERPROFILE%\Desktop\ 

::move the uninstaller file to the game folder
move gamefiles\bat-files\uninstall-DoGeX.bat %USERPROFILE%\Documents\Dont-Get-Expelled\ 

::move the manual file to the game folder
move gamefiles\bat-files\Game-Manual.bat %USERPROFILE%\Documents\Dont-Get-Expelled\ 

::delete the python installer
del /Q %USERPROFILE%\Downloads\python-3.10.4-amd64.exe 

::create a temporary folder
mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\temporary 

::delete the main directory
rmdir /Q /s Dont-Get-Expelled-main 

::clear the screen
cls 

echo The program is now installed, RESTART the system and open the STARTER-Dont-Get-Expelled.bat file
echo.
echo Game manual and uninstaller is located in the Documents folder

pause

::delete the installer file
del /Q /F %USERPROFILE%\Downloads\DoGeX-setup.bat 
