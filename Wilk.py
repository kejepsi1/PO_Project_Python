from Zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(9,5,polozenie_x,polozenie_y, swiat, 'W')

    def rysuj(self):
        self._swiat.narysuj_organizm(self._polozenie_x, self._polozenie_y, 'W')

    def rozmnazaj(self, x, y):
        return Wilk(x, y, self._swiat)

    def czy_drapieznik(self):
        return True
