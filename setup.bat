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

		echo installing Python, WAIT PATIENTLY! `&& curl https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe -o %USERPROFILE%\Downloads\python-3.10.4-amd64.exe
		
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

echo Python is now going to install the required libraries, OK?	
pause

python -m pip install pygame %*
python -m pip install pytmx %* 

echo.
echo libraries are now installed		
echo.  

echo Now the program will be installed
echo.

#TODO add a check for the program being installed

echo The program is now installed, reboot the system and open the START Dont-Get-Expelled - The Batory game.bat file
pause
