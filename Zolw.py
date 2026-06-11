import random
from Zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(2, 1, polozenie_x, polozenie_y, swiat, 'Z')

    def rysuj(self):
        self._swiat.narysuj_organizm(self.polozenie_x, self.polozenie_y, 'Z')

    def akcja(self, klawisz=None):
        if self.wiek == 0:
            return

        self._stare_polozenie_x = self.polozenie_x
        self._stare_polozenie_y = self.polozenie_y

        czy_rusza = random.randint(0, 3)

        if czy_rusza == 3:
            nowe_x = self.polozenie_x
            nowe_y = self.polozenie_y
            ruch = random.randint(0, 7)

            if ruch == 0:
                nowe_x += 1
            elif ruch == 1:
                nowe_x -= 1
            elif ruch == 2:
                nowe_y += 1
            elif ruch == 3:
                nowe_y -= 1
            elif ruch == 4:
                nowe_x -= 1
                nowe_y -= 1
            elif ruch == 5:
                nowe_x -= 1
                nowe_y += 1
            elif ruch == 6:
                nowe_x += 1
                nowe_y -= 1
            elif ruch == 7:
                nowe_x += 1
                nowe_y += 1

            if 0 <= nowe_x < self._swiat.x and 0 <= nowe_y < self._swiat.y:
                self.polozenie_x = nowe_x
                self.polozenie_y = nowe_y

    def czy_odpycha(self, napastnik):
        if napastnik.sila < 5:
            napastnik.cofnij()
            self._swiat.dodaj_komunikat("Zolw chowa sie w skorupie i odpycha atak")
            return True

        return False

    def rozmnazaj(self, x, y):
        return Zolw(x, y, self._swiat)