import requests
import json

url = "https://api.chucknorris.io/jokes/random"

try:
    response = requests.get(url)
    data = response.json()

    if "value" in data:
        vitsi = data["value"]
        print("Chuck norris sanoo:")
        print(vitsi)
    else:
        print("Vitsin hakeminen epäonnistui.")
except Exception as e:
    print("Virhe: {e}")