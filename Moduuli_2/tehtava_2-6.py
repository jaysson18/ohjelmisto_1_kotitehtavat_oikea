import random

koodi1 = ""
for i in range (3):
    numero = random.randint(0, 9)
    koodi1 += str(numero)


koodi2 = ""
for i in range(4):
    numero = random.randint(1,6)
    koodi2 += str(numero)

print(f"Kolmenumeroinen koodi: {koodi1}")
print(f"Nelinumeroinen koodi: {koodi2}")
