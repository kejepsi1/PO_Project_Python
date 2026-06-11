import random
from Zwierze import Zwierze

class Lis(Zwierze):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(3, 7, polozenie_x, polozenie_y, swiat, 'L')

    def rysuj(self):
        self._swiat.narysuj_organizm(self.polozenie_x, self.polozenie_y, 'L')

    def akcja(self, klawisz=None):
        if self.wiek == 0:
            return

        self._stare_polozenie_x = self.polozenie_x
        self._stare_polozenie_y = self.polozenie_y

        mozliwe_x = [-1, 1, 0, 0, -1, -1, 1, 1]
        mozliwe_y = [0, 0, -1, 1, -1, 1, -1, 1]
        bezpieczne = []

        for i in range(len(mozliwe_x)):
            potencjalne_x = self.polozenie_x + mozliwe_x[i]
            potencjalne_y = self.polozenie_y + mozliwe_y[i]

            if 0 <= potencjalne_x < self._swiat.x and 0 <= potencjalne_y < self._swiat.y:
                if self.dobry_wech(potencjalne_x, potencjalne_y):
                    bezpieczne.append(i)

        if bezpieczne:
            wybrany = random.choice(bezpieczne)
            self.polozenie_x += mozliwe_x[wybrany]
            self.polozenie_y += mozliwe_y[wybrany]

    def dobry_wech(self, x, y):
        for organizm in self._swiat.organizmy:
            if organizm.polozenie_x == x and organizm.polozenie_y == y:
                if organizm.czy_zyje() and self.sila < organizm.sila:
                    return False
        return True

    def rozmnazaj(self, x, y):
        return Lis(x, y, self._swiat)

    def czy_drapieznik(self):
        return True