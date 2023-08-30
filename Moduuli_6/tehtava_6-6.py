def laske_yksikkohinta(halkaisija, hinta):
    pinta_ala = (halkaisija / 2)**2 * 3.14159
    yksikköhinta = hinta / pinta_ala
    return yksikköhinta

def main():
    halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm):"))
    hinta1 = float(input("Syötä ensimmäisen pizzan hinta (€): "))
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)

    halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä toisen pizzan hinta (€): "))
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    if yksikkohinta1 < yksikkohinta2:
        parempi_pizza = "ensimmäinen pizza"
    else:
        parempi_pizza = "toinen pizza"

    print(f"Ensimmäsisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m2")
    print(f"Toinen pizzan yksikköhinta: {yksikkohinta2:.2f} €/m2")
    print(f"{parempi_pizza} antaa paremman vastineen rahalle.")

if __name__ == '__main__':
    main()