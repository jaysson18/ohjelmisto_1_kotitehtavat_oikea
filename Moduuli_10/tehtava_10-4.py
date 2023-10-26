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


class Kilpailu:
    def __init__(self, nimi, kilometrit, autot):
        self.nimi = nimi
        self.kilometritavoite = kilometrit
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("{:<10} {:<15} {:<10} {:<20}".format("Rekisteri", "Huippunopeus (km/h)", "Nopeus (km/h)",
                                                   "Kuljettu Matka (km)"))
        for auto in self.autot:
            print("{:<10} {:<15} {:<10} {:<20}".format(auto.rekkari, auto.huippunopeus, auto.nykyinen_nopeus,
                                                       auto.kuljettu_matka))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.kilometritavoite:
                return True
        return False


# Luo 10 autoa kilpailuun
kilpaautojen_lista = []
for i in range(10):
    rekkari = f"ABC-{i + 1}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekkari, huippunopeus)
    kilpaautojen_lista.append(auto)

kilometritavoite = 8000  # Kilpailun tavoitekilometrit
kilpailu = Kilpailu("Suuri romuralli", kilometritavoite, kilpaautojen_lista)

# Kilpailu
kilpailu_käynnissä = True
tunnit = 0
tulostusvali = 10

while kilpailu_käynnissä:
    tunnit += 1
    kilpailu.tunti_kuluu()

    if tunnit % tulostusvali == 0:
        print(f"Tunti {tunnit}")
        kilpailu.tulosta_tilanne()

    if kilpailu.kilpailu_ohi():
        kilpailu_käynnissä = False

# Tulosta kilpailun tulokset
print("\nKilpailun tulokset:")
kilpailu.tulosta_tilanne()
