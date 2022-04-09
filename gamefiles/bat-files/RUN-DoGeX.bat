@echo off

del /Q %USERPROFILE%\Documents\Dont-Get-Expelled\temporary

curl https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/testy/gamefiles/version.txt -o %USERPROFILE%\Documents\Dont-Get-Expelled/temporary\version.txt 

set /p origin=< %USERPROFILE%\Documents\Dont-Get-Expelled\temporary\version.txt

set /p local=< %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles\version.txt

cls

if %local% == %origin% (
    echo.
    echo "You have the latest version"
    echo.

    timeout /t 2
    echo.

    cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

    python dontgetexpelled.py 

) else (
    echo You don't have the latest version
    echo.
    timeout /t 3
    echo.
    echo Downloading...

    rmdir /Q /s %USERPROFILE%\Documents\Dont-Get-Expelled

    mkdir %USERPROFILE%\Documents\Dont-Get-Expelled

    curl -L https://github.com/TabeFlipStudio/Dont-Get-Expelled/archive/refs/heads/main.zip -o %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip

    powershell expand-archive %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip %USERPROFILE%\Documents\Dont-Get-Expelled\

    cd /d %USERPROFILE%\Desktop

    cd /d %USERPROFILE%\Documents\Dont-Get-Expelled

    del /Q /F Dont-Get-Expelled.zip

    move Dont-Get-Expelled-main\gamefiles %USERPROFILE%\Documents\Dont-Get-Expelled\

    move gamefiles\bat-files\START-DoGeX.bat %USERPROFILE%\Desktop\

    move gamefiles\bat-files\uninstall-DoGeX.bat %USERPROFILE%\Documents\Dont-Get-Expelled\

    mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\temporary

    rmdir /Q /s Dont-Get-Expelled-main
    cls

    echo the game has been updated and is now installed, please restart the system and open the START-Dont-Get-Expelled.bat file
    pause
    
    del /Q /F %USERPROFILE%\Desktop\RUN-DoGeX.bat

)
    

