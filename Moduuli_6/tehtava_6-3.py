def muunna_gallonoiksi(litramäärä):
    return litramäärä / 3.785

def main():
    while True:
        gallonat = float(input("Syötä bensiinin määrä gallonoina (negatiivinen lopettaa): "))
        if gallonat < 0:
            break
        litrat = muunna_gallonoiksi(gallonat)
        print(f"{gallonat} gallonaa on {litrat:.2f} litraa")


if __name__ == "__main__":
    main()