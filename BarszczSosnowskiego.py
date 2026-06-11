import random
from Roslina import Roslina
from Zwierze import Zwierze


class BarszczSosnowskiego(Roslina):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(10, 0, polozenie_x, polozenie_y, swiat, 'B')

    def rysuj(self):
        self._swiat.narysuj_organizm(self.polozenie_x, self.polozenie_y, 'B')

    def akcja(self, klawisz=None):
        if self.wiek == 0:
            return

        mozliwe_x = [-1, 1, 0, 0, -1, -1, 1, 1]
        mozliwe_y = [0, 0, -1, 1, -1, 1, -1, 1]

        for j in range(8):
            potencjalne_x = self.polozenie_x + mozliwe_x[j]
            potencjalne_y = self.polozenie_y + mozliwe_y[j]

            for sasiad in self._swiat.organizmy:
                if sasiad.polozenie_x == potencjalne_x and sasiad.polozenie_y == potencjalne_y:
                    if sasiad.czy_zyje() and isinstance(sasiad, Zwierze):
                        if not sasiad.uniknij_smierci(self):
                            tekst = f"Barszcz Sosnowskiego zabija: {sasiad.znak}"
                            self._swiat.dodaj_komunikat(tekst)
                            sasiad.zabij()

        draw = random.randint(0, 19)
        if draw == 0:
            bezpieczne = []
            for i in range(len(mozliwe_x)):
                potencjalne_x = self.polozenie_x + mozliwe_x[i]
                potencjalne_y = self.polozenie_y + mozliwe_y[i]

                if 0 <= potencjalne_x < self._swiat.x and 0 <= potencjalne_y < self._swiat.y:
                    if self.sprawdzaj_sasiadow(potencjalne_x, potencjalne_y):
                        bezpieczne.append(i)

            if bezpieczne:
                wybrany = random.choice(bezpieczne)
                self._swiat.dodaj_komunikat("Powstaje nowy Barszcz Sosnowskiego")

                nowe_x = self.polozenie_x + mozliwe_x[wybrany]
                nowe_y = self.polozenie_y + mozliwe_y[wybrany]
                self._swiat.dodaj_organizm(BarszczSosnowskiego(nowe_x, nowe_y, self._swiat))

    def sprawdzaj_sasiadow(self, x, y):
        for organizm in self._swiat.organizmy:
            if x == organizm.polozenie_x and y == organizm.polozenie_y:
                return False
        return True

    def czy_obronil(self, napastnik):
        self._swiat.dodaj_komunikat("Zwierze zjadlo Barszcz Sosnowskiego i zginelo")
        self.zabij()
        return True