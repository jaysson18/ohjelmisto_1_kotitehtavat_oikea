kuukaudet_vuodenajat = {
    1: "Talvi",
    2: "Talvi",
    3: "Kevät",
    4: "Kevät",
    5: "Kevät",
    6: "Kesä",
    7: "Kesä",
    8: "Kesä",
    9: "Syksy",
    10: "Syksy",
    11: "Syksy",
    12: "Talvi",
}


kuukausi_numero = int(input("Anna kuukauden numero (1-12): "))

if kuukausi_numero >= 1 and kuukausi_numero <= 12:
    vuodenaika = kuukaudet_vuodenajat[kuukausi_numero]
    print(f"Kuukausi {kuukausi_numero} kuuluu vuodenaikaan {vuodenaika}.")
else:
    print("Virheellinen kuukauden numero. Anna luku väliltä 1-12")