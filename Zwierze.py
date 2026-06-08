from Organizm import Organizm
import random

class Zwierze(Organizm):
    def __init__(self, sila, inicjatywa, polozenie_x, polozenie_y, swiat, znak):
        super().__init__(sila, inicjatywa, polozenie_x, polozenie_y, swiat, znak)

    def rozmnoz_sie(self):
        mozliwe_x = [-1,1,0,0,-1,-1,1,1]
        mozliwe_y = [0,0,-1,1,-1,1,-1,1]
        bezpieczne = []
        for j in range(len(mozliwe_x)):
            potencjalne_x = self._polozenie_x + mozliwe_x[j]
            potencjalne_y = self._polozenie_y + mozliwe_y[j]
            if 0 <= potencjalne_x < self._swiat.x and 0 <= potencjalne_y < self._swiat.y:
                zajete = False
                for organizm in self._swiat.organizmy:
                    if organizm.czy_zyje() and organizm._polozenie_x == potencjalne_x and organizm._polozenie_y == potencjalne_y:
                        zajete = True
                        break

                if not zajete:
                    bezpieczne.append(j)

        if bezpieczne:
            wybrany = random.choice(bezpieczne)
            nowe_x = self._polozenie_x + mozliwe_x[wybrany]
            nowe_y = self._polozenie_y + mozliwe_y[wybrany]
            dziecko = self.rozmnazaj(nowe_x,nowe_y)
            if dziecko is not None:
                self._swiat.dodaj_organizm(dziecko)
                dziecko._wiek = 0