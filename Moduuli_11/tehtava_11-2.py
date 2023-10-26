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

class Sähköauto(Auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, huippunopeus, bensatankki_koko):
        super().__init__(rekkari, huippunopeus)
        self.bensatankki_koko = bensatankki_koko

# Luo sähköauto ja polttomoottoriauto
sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

# Aseta nopeudet
sähköauto.kiihdytä(100)
polttomoottoriauto.kiihdytä(120)

# Aja autoja 3 tuntia
ajettu_aika = 3  # tuntia
sähköauto.kulje(ajettu_aika)
polttomoottoriauto.kulje(ajettu_aika)

# Tulosta matkamittarilukemat
print(f"Sähköauton matkamittarilukema: {sähköauto.kuljettu_matka} km")
print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")
