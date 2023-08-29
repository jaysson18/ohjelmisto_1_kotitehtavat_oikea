yritykset = 0

while yritykset < 5:

    kayttajatunnus = input("Anna Käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if kayttajatunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudestaan.")
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty!")