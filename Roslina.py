from Organizm import Organizm

class Roslina(Organizm):
    def __init__(self, sila, inicjatywa, polozenie_x,polozenie_y, swiat, znak):
        super().__init__(sila, inicjatywa, polozenie_x, polozenie_y, swiat, znak)

    def kolizja(self):
        pass

    def sprawdzaj_sasiadow(self, x, y):
        for organizm in self._swiat.organizmy:
            if organizm.czy_zyje() and x == organizm.polozenie_x and y == organizm.polozenie_y:
                return False

        return True
