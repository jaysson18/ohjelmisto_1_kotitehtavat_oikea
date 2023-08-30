kaupungit = []


for i in range(5):
    kaupunki = input("Syötä kaupungin nimi, paina enter jotta ohjelma loppuu!: ")
    kaupungit.append(kaupunki)


print("Syöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)