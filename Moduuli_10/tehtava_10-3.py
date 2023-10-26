class Hissi:
    def __init__(self, alin_kerros, ylimpaan_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylimpaan_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros:
            kohde_kerros = self.alin_kerros
        elif kohde_kerros > self.ylin_kerros:
            kohde_kerros = self.ylin_kerros

        while self.kerros > kohde_kerros:
            self.kerros_alas()
        while self.kerros < kohde_kerros:
            self.kerros_ylös()

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f'Hissi nousi kerrokseen {self.kerros}')

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f'Hissi laski kerrokseen {self.kerros}')


class Talo:
    def __init__(self, alin_kerros, ylimpaan_kerros, hissien_lukumaara):
        self.hissit = [Hissi(alin_kerros, ylimpaan_kerros)for _ in range(hissien_lukumaara)]

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        if hissin_numero >= 0 and hissin_numero < len(self.hissit):
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Hissiä numero {hissin_numero} ei ole talossa.")

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.hissit[0].alin_kerros)
        print("Palohälytys: kaikki hissit ovat pohjakerroksessa.")


if __name__ == '__main__':
    talo = Talo(alin_kerros=1, ylimpaan_kerros=10, hissien_lukumaara= 2)

    talo.aja_hissiä(0 ,5)
    talo.aja_hissiä(1, 7)
    talo.aja_hissiä(2, 3)

    for i, hissi in enumerate(talo.hissit):
        print(f"Hissi {i} on kerroksessa {hissi.kerros}")


    talo.palohälytys()