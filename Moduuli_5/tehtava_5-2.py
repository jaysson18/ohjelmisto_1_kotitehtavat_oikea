# Luo tyhjä lista johon luvut tallennetaan
luvut = []

# Kysy käyttäjältä lukuja, kunnes käyttäjä syöttää tyhjän merkkijonon
while True:
    syote = input("Syötä luku (tai jätä tyhjäksi lopettaaksesi): ")

    # Lopeta silmukka, jos syöte on tyhjä merkkijono
    if syote == "":
        break

    # Yritä muuntaa syöte luvuksi ja tallentaa se listaan
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötä oikea luku.")

# Järjestä luvut suuruusjärjestykseen ja käännä lista
luvut.sort(reverse=True)

# Tulosta viisi suurinta lukua listasta (jos lista on ylipäänsä niin pitkä)
print("Viisi suurinta lukua ovat:")
for i in range(min(5, len(luvut))):
    print(luvut[i])
