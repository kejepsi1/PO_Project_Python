import random
from Zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(4, 4, polozenie_x, polozenie_y, swiat, 'A')

    def rysuj(self):
        self._swiat.narysuj_organizm(self.polozenie_x, self.polozenie_y, 'A')

    def akcja(self, klawisz=None):
        if self.wiek == 0:
            return

        self._stare_polozenie_x = self.polozenie_x
        self._stare_polozenie_y = self.polozenie_y

        mozliwe_x = [1, -1, 0, 0, -1, -1, 1, 1]
        mozliwe_y = [0, 0, 1, -1, -1, 1, -1, 1]

        ruch = random.randint(0, 7)
        dystans = random.randint(1, 2)

        nowe_x = self.polozenie_x + (mozliwe_x[ruch] * dystans)
        nowe_y = self.polozenie_y + (mozliwe_y[ruch] * dystans)

        if 0 <= nowe_x < self._swiat.x and 0 <= nowe_y < self._swiat.y:
            self.polozenie_x = nowe_x
            self.polozenie_y = nowe_y

    def kolizja(self):
        self._swiat.sprawdzaj_kolizje(self)

    def czy_odpycha(self, napastnik):
        if random.randint(0, 1) == 0:
            return False

        mozliwe_x = [-1, 1, 0, 0, -1, -1, 1, 1]
        mozliwe_y = [0, 0, -1, 1, -1, 1, -1, 1]
        bezpieczne = []

        for j in range(len(mozliwe_x)):
            potencjalne_x = self.polozenie_x + mozliwe_x[j]
            potencjalne_y = self.polozenie_y + mozliwe_y[j]

            if 0 <= potencjalne_x < self._swiat.x and 0 <= potencjalne_y < self._swiat.y:
                zajete = False
                for organizm in self._swiat.organizmy:
                    if organizm.polozenie_x == potencjalne_x and organizm.polozenie_y == potencjalne_y:
                        zajete = True
                        break

                if not zajete:
                    bezpieczne.append(j)

        if bezpieczne:
            wybrany = random.choice(bezpieczne)

            self._stare_polozenie_x = self.polozenie_x
            self._stare_polozenie_y = self.polozenie_y

            self.polozenie_x += mozliwe_x[wybrany]
            self.polozenie_y += mozliwe_y[wybrany]

            tekst = f"Antylopa uciekla przed: {napastnik.znak}"
            self._swiat.dodaj_komunikat(tekst)

            return True

        return False

    def rozmnazaj(self, x, y):
        return Antylopa(x, y, self._swiat)