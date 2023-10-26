import requests

API_KEY = "1790270ca56a664b613e0518401b93ca"

def hae_saa(paikkakunta):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": paikkakunta,
        "appid": API_KEY
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()


        if data["cod"] == 200:
            sateen_tyyppi = data["weather"][0]["description"]
            lampotila_kelvin = data["main"]["temp"]
            lampotila_celsius = lampotila_kelvin - 273.15

            print(f"Säätila paikkakunnalla {paikkakunta}: {sateen_tyyppi}")
            print(f"Lämpötila: {lampotila_celsius:.2f} °C")
        else:
            print("Säätietojen hakeminen epäonnistui.")
    except Exception as e:
        print(f"Virhe: {e}")

if __name__ == "__main__":
    paikkakunta = input("Anna paikkakunnan nimi: ")
    hae_saa(paikkakunta)