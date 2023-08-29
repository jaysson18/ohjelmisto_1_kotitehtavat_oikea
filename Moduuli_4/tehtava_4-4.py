import random

# Arpoo kokonaisluvun väliltä 1-10
arvattava_luku = random.randint(1, 10)

while True:
    # Pyytää pelaajaa arvaamaan luvun
    arvaus = input("Arvaa luku väliltä 1-10: ")

    try:

        arvaus = int(arvaus)


        if arvaus < arvattava_luku:
            print("Liian pieni arvaus.")
        elif arvaus > arvattava_luku:
            print("Liian suuri arvaus.")
        else:
            print("Oikein!")
            break
    except ValueError:
        print("Ei kelvollinen kokonaisluku. Yritä uudestaan.")
