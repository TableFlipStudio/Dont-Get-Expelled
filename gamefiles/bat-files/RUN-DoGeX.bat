@echo off

curl https://api.github.com/repos/TabeFlipStudio/Dont-Get-Expelled/gamefiles/version.txt %USERPROFILE%\Documents\Dont-Get-Expelled/temporary\version.txt | grep "browser_download_url.*exe" | cut -d : -f 2,3 | tr -d \" | wget -i -

set /p origin=< %USERPROFILE%\Documents\Dont-Get-Expelled\temporary\version.txt
# TODO: this the downloaded file


set /p local=< %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles\version.txt

if %mytextfile% == %mytextfile2% (
echo "You have the latest version"
)

if %origin% > %local% (
    echo You don't have the latest version
    echo.
    echo Downloading...


)
    

cd /d %USERPROFILE%\Documents\Dont-Get-Expelled\gamefiles

python dontgetexpelled.py && exit /B
