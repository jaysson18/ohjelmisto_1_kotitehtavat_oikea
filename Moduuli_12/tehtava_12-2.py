import requests

api_key = "1790270ca56a664b613e0518401b93ca"

def hae_saatieto(paikkakunta):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": paikkakunta,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        saa = data["weather"][0]["description"]
        lampotila = data["main"]["temp"]
        print(f"Sää paikkakunnalla {paikkakunta}: {saa.capitalize()}")
        print(f"Lämpötila: {lampotila} °C")
    else:
        print("Säätilan hakeminen epäonnistui.")

if __name__ == "__main__":
    paikkakunta = input("Syötä paikkakunnan nimi: ")
    hae_saatieto(paikkakunta)
