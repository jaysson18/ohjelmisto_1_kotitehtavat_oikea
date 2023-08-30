import random

def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

def main():
    tahkojen_maara = int(input("Syötä nopan tahkojen yhteismäärä: "))
    maksimisilmaluku = int(input("Syötä nopan maksimisilmäluku: "))

    while True:
        heitto = heita_noppaa(tahkojen_maara)
        print(f"Heitto: {heitto}")
        if heitto == maksimisilmaluku:
            break


if __name__ == '__main__':
    main()