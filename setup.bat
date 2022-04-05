@echo off

cls #clear the screen


start /W msedge.exe "https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe"
taskkill/im msedge.exe

pause

#python -m pip install pygame %*
#python -m pip install pytmx %* 
