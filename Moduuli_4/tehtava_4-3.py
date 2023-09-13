pienin_luku = None
suurin_luku = None

while True:
    syote = input("Anna luku (lopettaaksesi, jätä kenttä tyhjäksi): ")

    if syote == "":
        break

    try:

        luku = float(syote)

        if pienin_luku is None or luku < pienin_luku:
            pienin_luku = luku
        if suurin_luku is None or luku > suurin_luku:
            suurin_luku = luku

    except ValueError:
        print("Ei kelvollinen numero. Yritä uudestaan.")

if pienin_luku is not None and suurin_luku is not None:
    print(f"Pienin luku: {pienin_luku}")
    print(f"Suurin luku: {suurin_luku}")
