import requests

response = requests.get("https://data.directory.opinbrasil.com.br/participants")
print(response.json())