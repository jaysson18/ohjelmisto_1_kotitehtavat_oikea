def main():
    try:
        kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: "))

        alin_sallittu_pituus = 37.0

        if kuhan_pituus < alin_sallittu_pituus:
            puuttuva_pituus = alin_sallittu_pituus - kuhan_pituus
            print(f"Kuha on alimittainen. Laske se takaisin järveen. Puuttuu: {puuttuva_pituus} cm.")
        else:
            print(f"Kuha on yli alimman sallitun pyyntimitan. Voit pitää sen.")


    except ValueError:
        print(f"Antamasi arvo ei ole kelvollinen numero. Yritä uudestaan.")

if __name__ == "__main__":
    main()