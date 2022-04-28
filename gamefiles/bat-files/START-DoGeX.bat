@echo off

::delete the old version checker folder
del /Q %USERPROFILE%\Documents\Dont-Get-Expelled\temporary

::download the new version checker folder
curl https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/version.txt -o %USERPROFILE%\Documents\Dont-Get-Expelled\temporary\version.txt 

::set the variable to the old and current version
set /p origin=< %USERPROFILE%\Documents\Dont-Get-Expelled\temporary\version.txt
set /p local=< %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles\version.txt

cls

::check if the game is up to date
if %local% == %origin% (
    echo.
    echo "You have the latest version"
    echo.
    
    ::goto the game folder
    cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

    ::start the game
    python3 dontgetexpelled.py 

) else (
    echo You don't have the latest version
    echo.
    timeout /t 2
    echo.
    echo Downloading...

    ::remove the old game version folder
    rmdir /Q /s %USERPROFILE%\Documents\Dont-Get-Expelled

    ::make a new folder
    mkdir %USERPROFILE%\Documents\Dont-Get-Expelled

    ::download the new version
    curl -L https://github.com/TabeFlipStudio/Dont-Get-Expelled/archive/refs/heads/main.zip -o %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip

    ::unpack the new version
    powershell expand-archive %USERPROFILE%\Documents\Dont-Get-Expelled\Dont-Get-Expelled.zip %USERPROFILE%\Documents\Dont-Get-Expelled\

    ::go to the game folder
    cd /d %USERPROFILE%\Documents\Dont-Get-Expelled

    ::delete the zip file
    del /Q /F Dont-Get-Expelled.zip

    ::move the game files to the game folder
    move Dont-Get-Expelled-main\gamefiles %USERPROFILE%\Documents\Dont-Get-Expelled\

    ::move the starter file to the desktop
    move gamefiles\bat-files\START-DoGeX.bat %USERPROFILE%\Desktop\

    ::move the uninstaller file to the game folder
    move gamefiles\bat-files\uninstall-DoGeX.bat %USERPROFILE%\Documents\Dont-Get-Expelled\

    ::move the manual file to the game folder
    mkdir %USERPROFILE%\Documents\Dont-Get-Expelled\temporary

    ::remove the main-git folder
    rmdir /Q /s Dont-Get-Expelled-main
    cls

    echo the game has been updated and is now installed, please restart the system and open the START-Dont-Get-Expelled.bat file
    pause
    
    ::
    del /Q /F %USERPROFILE%\Desktop\START-DoGeX.bat

)

exit /B
    

