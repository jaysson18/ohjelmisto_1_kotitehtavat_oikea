def main():
    try:
        vuosi = int(input("Anna vuosiluku: "))
    except ValueError:
        print("Virheellinen syöte. Käytä kokonaislukumuotoa.")
        return

    if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
        print(f"{vuosi} on karkausvuosi.")
    else:
        print(f"{vuosi} ei ole karkausvuosi.")


if __name__ == '__main__':
    main()

