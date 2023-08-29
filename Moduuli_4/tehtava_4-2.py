while True:
    tuumat = float(input("Anna tuumamäärä (lopettaaksesi, anna negatiivinen luku): "))

    if tuumat < 0:
        print("Ohjelma lopetettu.")
        break

    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuuma on {senttimetrit} senttimetreinä.")