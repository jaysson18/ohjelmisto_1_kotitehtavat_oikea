import random

# kysy käyttäjältä arpakuutioiden lukumäärä
n = int(input("Kuinka monta arpakuutiota haluat heittää?"))

# alustetaan silmälukujen summa nollaksi
summa = 0

# heitä jokaista arpakuutiota kerran ja lisää tulokset summaan
for i in range(n):
    heitto = random.randint(1, 6)
    summa += heitto

# tulosta silmälukujen summa
print(f"Silmälukujen summa on {summa}")
