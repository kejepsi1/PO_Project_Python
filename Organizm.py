import random

class Organizm:
    def __init__(self, sila, inicjatywa, polozenie_x, polozenie_y, swiat, znak):
        self._czy_zyje = True
        self._stare_polozenie_y = polozenie_y
        self._stare_polozenie_x = polozenie_x
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._polozenie_x = polozenie_x
        self._polozenie_y = polozenie_y
        self._swiat = swiat
        self._znak = znak
        self._wiek = 0

    @property
    def sila(self):
        return self._sila
    @property
    def inicjatywa(self):
        return self._inicjatywa
    @property
    def polozenie_x(self):
        return self._polozenie_x
    @property
    def polozenie_y(self):
        return self._polozenie_y
    @property
    def znak(self):
        return self._znak
    @property
    def wiek(self):
        return self._wiek

    @sila.setter
    def sila(self, sila):
        self._sila = sila
    @polozenie_x.setter
    def polozenie_x(self, polozenie_x):
        self._polozenie_x = polozenie_x
    @polozenie_y.setter
    def polozenie_y(self, polozenie_y):
        self._polozenie_y = polozenie_y
    @wiek.setter
    def wiek(self, wiek):
        self._wiek = wiek

    def czy_odpycha(self, napastnik):
        return False

    def akcja(self, klawisz):
        if self.wiek == 0:
            return
        self._stare_polozenie_x = self._polozenie_x
        self._stare_polozenie_y = self._polozenie_y

        noweX = self._polozenie_x
        noweY = self._polozenie_y
        ruch = random.randint(0, 7)
        if ruch == 0:
            noweX += 1
        elif ruch == 1:
            noweX -= 1
        elif ruch == 2:
            noweY += 1
        elif ruch == 3:
            noweY -= 1
        elif ruch == 4:
            noweX -= 1
            noweY -= 1
        elif ruch == 5:
            noweX += 1
            noweY -= 1
        elif ruch == 6:
            noweX -= 1
            noweY += 1
        elif ruch == 7:
            noweX += 1
            noweY += 1

        if 0 <= noweX < self._swiat.x and 0 <= noweY < self._swiat.y:
            self._polozenie_x = noweX
            self._polozenie_y = noweY

    def kolizja(self):
        self._swiat.sprawdzaj_kolizje(self)

    def cofnij(self):
        self._polozenie_x = self._stare_polozenie_x
        self._polozenie_y = self._stare_polozenie_y

    def rozmnazaj(self, x, y):
        return None

    def rozmnoz_sie(self):
        pass

    def czy_zyje(self):
        return self._czy_zyje

    def zabij(self):
        self._czy_zyje = False

    def czy_mozna_zdeptac(self, napastnik):
        return False

    def czy_drapieznik(self):
        return False

    def uniknij_smierci(self, napastnik):
        return False

    def czy_obronil(self, napastnik):
        if napastnik.sila >= self.sila:
            return False
        return True
