from Zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(4,4,polozenie_x,polozenie_y, swiat, 'O')

    def rysuj(self):
        self._swiat.narysuj_organizm(self._polozenie_x, self._polozenie_y, 'O')

    def rozmnazaj(self, x, y):
        return Owca(x, y, self._swiat)

    def czy_drapieznik(self):
        return True
