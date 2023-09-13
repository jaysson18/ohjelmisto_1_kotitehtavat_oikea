lentoasemat = {}

while True:
    print("\nValitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Valitse toiminto numero (1/2/3):")

    if valinta == "1":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao_koodi] = nimi
        print("Lentoasema tallennettu onnistuuneesti.")

    elif valinta == "2":
        icao_koodi = input("Syötä lentoaseman ICAO-koodi, jonka tiedot haluat hakea: ")
        if icao_koodi in lentoasemat:
            print(f"Lentoasema nimi {lentoasemat[icao_koodi]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        print("Ohjelma päättyy.")
        break

    else:
        print("Vihreellinen valinta. Valitse 1, 2 tai 3")