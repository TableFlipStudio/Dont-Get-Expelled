import requests

r = requests.get('https://raw.githubusercontent.com/TableFlipStudio/Dont-Get-Expelled/main/gamefiles/version.txt', stream=True)
r.content