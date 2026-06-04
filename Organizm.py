import random

class Organizm:
    def __init__(self, sila, inicjatywa, polozenieX, polozenieY, swiat, znak):
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._polozenieX = polozenieX
        self._polozenieY = polozenieY
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
    def polozenieX(self):
        return self._polozenieX
    @property
    def polozenieY(self):
        return self._polozenieY
    @property
    def znak(self):
        return self._znak
    @property
    def wiek(self):
        return self._wiek

    @sila.setter
    def sila(self, sila):
        self._sila = sila
    @polozenieX.setter
    def polozenieX(self, polozenieX):
        self._polozenieX = polozenieX
    @polozenieY.setter
    def polozenieY(self, polozenieY):
        self._polozenieY = polozenieY
    @wiek.setter
    def wiek(self, wiek):
        self._wiek = wiek

    def CzyOdpycha(self, napastnik):
        return False

    def Akcja(self):
        if self.wiek == 0:
            return
        stare_polozenieX = self._polozenieX
        stare_PolozenieY = self._polozenieY

        noweX = self._polozenieX
        noweY = self._polozenieY
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

        if noweX >= 0 and noweX < swiat.X and noweY >= 0 and noweY < swiat.Y:
            self._polozenieX = noweX
            self._polozenieY = noweY
