leiviskat = float(input("Anna massan määrä leivisköinä: "))
naulat = float(input("Anna massan määrä nauloina: "))
luodit = float(input("Anna massan määrä luoteina: "))

# muunnetaan kaikki grammoiksi
grammat_leiviskat = leiviskat * 20 *  32 * 13.3
grammat_naulat = naulat * 32 * 13.3
grammat_luodit = luodit * 13.3

yhteismassa_grammat = grammat_leiviskat + grammat_naulat + grammat_luodit

yhteismassa_kg = int(yhteismassa_grammat // 1000)
yhteismassa_jaannos_g = yhteismassa_grammat % 1000

print(f"Yhteismassa on {yhteismassa_kg} kilogrammaa ja {yhteismassa_jaannos_g} grammaa.")