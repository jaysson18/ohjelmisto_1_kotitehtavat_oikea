def laske_summa(lista):
    return sum(lista)

def main():
    luvut = [5, 10, 15, 20, 25]
    summa = laske_summa(luvut)
    print(f"Listan lukujen summa {summa}")


if __name__ == '__main__':
    main()