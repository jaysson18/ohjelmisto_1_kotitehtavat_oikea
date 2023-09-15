class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

#Pääohjelma

if __name__ == '__main__':
    uusi_auto = Auto("ABC-123", 142) # Uuden auton luonti
    print("Luodun auton ominaisuudet:")
    print(f"Rekisteritunnus: {uusi_auto.rekkari}")
    print(f"Huippunopeus: {uusi_auto.huippunopeus}")
    print(f"Nykyinen nopeus: {uusi_auto.nykyinen_nopeus} km/h")
    print(f"Kuljettu matka: {uusi_auto.kuljettu_matka} km")
