import random
from Roslina import Roslina


class WilczeJagody(Roslina):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(99, 0, polozenie_x, polozenie_y, swiat, 'J')

    def rysuj(self):
        self._swiat.narysuj_organizm(self.polozenie_x, self.polozenie_y, 'J')

    def akcja(self, klawisz=None):
        if self.wiek == 0:
            return

        draw = random.randint(0, 19)
        if draw == 0:
            mozliwe_x = [-1, 1, 0, 0, -1, -1, 1, 1]
            mozliwe_y = [0, 0, -1, 1, -1, 1, -1, 1]
            bezpieczne = []

            for i in range(len(mozliwe_x)):
                potencjalne_x = self.polozenie_x + mozliwe_x[i]
                potencjalne_y = self.polozenie_y + mozliwe_y[i]

                if 0 <= potencjalne_x < self._swiat.x and 0 <= potencjalne_y < self._swiat.y:
                    if self.sprawdzaj_sasiadow(potencjalne_x, potencjalne_y):
                        bezpieczne.append(i)

            if bezpieczne:
                wybrany = random.choice(bezpieczne)

                self._swiat.dodaj_komunikat("Powstaja nowe Wilcze Jagody")

                nowe_x = self.polozenie_x + mozliwe_x[wybrany]
                nowe_y = self.polozenie_y + mozliwe_y[wybrany]

                self._swiat.dodaj_organizm(WilczeJagody(nowe_x, nowe_y, self._swiat))

    def czy_obronil(self, napastnik):
        self.zabij()

        return True