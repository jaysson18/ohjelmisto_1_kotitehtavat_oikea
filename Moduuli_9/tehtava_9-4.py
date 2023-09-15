import random

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos
        if uusi_nopeus >= 0 and uusi_nopeus <= self.huippunopeus:
            self.nykyinen_nopeus = uusi_nopeus
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = self.huippunopeus

    def kulje(self, tuntimäärä):
        eteneminen = self.nykyinen_nopeus * tuntimäärä
        self.kuljettu_matka += eteneminen

# Luo kymmenen autoa kilpailuun
kilpaautojen_lista = []
for i in range(10):
    rekkari = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekkari, huippunopeus)
    kilpaautojen_lista.append(auto)

kilometritavoite = 10000  # Kilpailun tavoitekilometrit

# Kilpailu
kilpailu_käynnissä = True
tunnit = 0

while kilpailu_käynnissä:
    tunnit += 1
    print(f"Tunti {tunnit}")

    # Muuta jokaisen auton nopeutta
    for auto in kilpaautojen_lista:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)

    # Liikuta jokaista autoa tunnin ajan
    for auto in kilpaautojen_lista:
        auto.kulje(1)

    # Tarkista, onko joku auto saavuttanut tavoitteen
    for auto in kilpaautojen_lista:
        if auto.kuljettu_matka >= kilometritavoite:
            kilpailu_käynnissä = False
            break

# Tulosta kilpailun tulokset
print("\nKilpailun tulokset:")
print("{:<10} {:<15} {:<10} {:<20}".format("Rekisteri", "Huippunopeus (km/h)", "Nopeus (km/h)", "Kuljettu Matka (km)"))
for auto in kilpaautojen_lista:
    print("{:<10} {:<15} {:<10} {:<20}".format(auto.rekkari, auto.huippunopeus, auto.nykyinen_nopeus, auto.kuljettu_matka))
