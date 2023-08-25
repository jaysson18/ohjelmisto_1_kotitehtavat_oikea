def main():
    sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ").lower()
    try:
        hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))
    except ValueError:
        print("Virheellinen syöte. Käytä numeromuotoa esim. 130.0")
        return

    if sukupuoli == "mies":
        if hemoglobiini < 134:
            print("Hemoglobiiniarvo on alhainen.")
        elif 134 <= hemoglobiini <= 195:
            print("Hemoglobiiniarvo on normaali.")
        else:
            print("Hemoglobiiniarvo on korkea.")
    elif sukupuoli == "nainen":
        if hemoglobiini < 117:
            print("Hemoglobiiniarvo on alhainen.")
        elif 117 <= hemoglobiini <= 175:
            print("Hemoglobiiniarvo on normaali.")
        else:
            print("Hemoglobiiniarvo on korkea.")
    else:
        print("Virheellinen sukupuoli. Syötä joko 'mies' tai 'nainen'.")


if __name__ == "__main__":
    main()