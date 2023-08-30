def poista_parittomat(lista):
    parilliset = [luku for luku in lista if luku % 2 == 0]
    return parilliset

def main():
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    parilliset_luvut = poista_parittomat(luvut)

    print("Alkuperäinen lista:", luvut)
    print("Parilliset luvut:", parilliset_luvut)

if __name__ == '__main__':
    main()