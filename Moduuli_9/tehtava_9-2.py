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


#pääohjelma

if __name__ == '__main__':
    uusi_auto =Auto("ABC-123", 142)

    print(" Auton nykyinen nopeus:")
    uusi_auto.kiihdytä(30)
    print(f"Nykyinen nopeus: {uusi_auto.nykyinen_nopeus} km/h")

    uusi_auto.kiihdytä(70)
    print(f"Nykyinen nopeus: {uusi_auto.nykyinen_nopeus} km/h")

    uusi_auto.kiihdytä(50)
    print(f"Nykyinen nopeus {uusi_auto.nykyinen_nopeus} km/h")

    #hätäjarrutus
    uusi_auto.kiihdytä(-200)
    print(f"Uusi nopeus hätäjarrutuksen jälkeen: {uusi_auto.nykyinen_nopeus} km/h")