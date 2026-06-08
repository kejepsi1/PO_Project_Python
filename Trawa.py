from Roslina import Roslina
import random

class Trawa(Roslina):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(0,0,polozenie_x, polozenie_y, swiat, 'T')

    def rysuj(self):
        self._swiat.narysuj_organizm(self._polozenie_x, self._polozenie_y, 'T')

    def akcja(self, klawisz):
        if self.wiek == 0:
            return

        draw = random.randint(0,19)
        if draw == 0:
            mozliwe_x = [-1,1,0,0,-1,-1,1,1]
            mozliwe_y = [0,0,-1,1,-1,1,-1,1]
            bezpieczne = []
            for i in range(len(mozliwe_x)):
                potencjalne_x = self._polozenie_x + mozliwe_x[i]
                potencjalne_y = self._polozenie_y + mozliwe_y[i]

                if 0 <= potencjalne_x < self._swiat.x and 0 <= potencjalne_y < self._swiat.y:
                    if self.sprawdzaj_sasiadow(potencjalne_x, potencjalne_y):
                        bezpieczne.append(i)

            if bezpieczne:
                wybrany = random.choice(bezpieczne)
                self._swiat.dodaj_organizm(Trawa(self._polozenie_x + mozliwe_x[wybrany], self._polozenie_y + mozliwe_y[wybrany], self._swiat))

    def czy_mozna_zdeptac(self, napastnik):
        if napastnik.czy_drapieznik():
            return True
        return False