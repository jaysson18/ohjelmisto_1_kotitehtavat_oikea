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


if __name__ == "__main__":
    hissi = Hissi(alin_kerros=1, ylimpaan_kerros=10)

    kohde_kerros = 5
    hissi.siirry_kerrokseen(kohde_kerros)

    hissi.siirry_kerrokseen(hissi.alin_kerros)
