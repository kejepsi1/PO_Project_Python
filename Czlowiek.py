import random
from Zwierze import Zwierze


class Czlowiek(Zwierze):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(5, 4, polozenie_x, polozenie_y, swiat, 'C')
        self._czas_trwania_umiejetnosci = 0
        self._czas_odnowienia_umiejetnosci = 0

    @property
    def czas_trwania_umiejetnosci(self):
        return self._czas_trwania_umiejetnosci

    @czas_trwania_umiejetnosci.setter
    def czas_trwania_umiejetnosci(self, wartosc):
        self._czas_trwania_umiejetnosci = wartosc

    @property
    def czas_odnowienia_umiejetnosci(self):
        return self._czas_odnowienia_umiejetnosci

    @czas_odnowienia_umiejetnosci.setter
    def czas_odnowienia_umiejetnosci(self, wartosc):
        self._czas_odnowienia_umiejetnosci = wartosc

    def akcja(self, klawisz=None):
        if klawisz == 'SPACE' and self.czas_odnowienia_umiejetnosci == 0:
            self.czas_odnowienia_umiejetnosci = 10
            self.czas_trwania_umiejetnosci = 5
            self._swiat.dodaj_komunikat("Czlowiek uzywa umiejetnosci niesmiertelnosc")
        elif self.czas_trwania_umiejetnosci != 0:
            self.czas_trwania_umiejetnosci -= 1
            self.czas_odnowienia_umiejetnosci -= 1
        elif self.czas_odnowienia_umiejetnosci != 0:
            self.czas_odnowienia_umiejetnosci -= 1

        self._stare_polozenie_x = self.polozenie_x
        self._stare_polozenie_y = self.polozenie_y

        nowe_x = self.polozenie_x
        nowe_y = self.polozenie_y

        if klawisz == 'UP':
            nowe_y -= 1
        elif klawisz == 'DOWN':
            nowe_y += 1
        elif klawisz == 'LEFT':
            nowe_x -= 1
        elif klawisz == 'RIGHT':
            nowe_x += 1
        elif klawisz == 'W':
            nowe_y -= 1
            nowe_x -= 1
        elif klawisz == 'R':
            nowe_y -= 1
            nowe_x += 1
        elif klawisz == 'X':
            nowe_y += 1
            nowe_x -= 1
        elif klawisz == 'V':
            nowe_y += 1
            nowe_x += 1

        if 0 <= nowe_x < self._swiat.x and 0 <= nowe_y < self._swiat.y:
            self.polozenie_x = nowe_x
            self.polozenie_y = nowe_y

    def rozmnazaj(self, x, y):
        return None

    def czy_drapieznik(self):
        return True

    def uniknij_smierci(self, napastnik):
        if self.czas_trwania_umiejetnosci > 0:
            mozliwe_x = [-1, 1, 0, 0, -1, -1, 1, 1]
            mozliwe_y = [0, 0, -1, 1, -1, 1, -1, 1]
            bezpieczne = []

            for i in range(len(mozliwe_x)):
                potencjalne_x = self.polozenie_x + mozliwe_x[i]
                potencjalne_y = self.polozenie_y + mozliwe_y[i]

                if 0 <= potencjalne_x < self._swiat.x and 0 <= potencjalne_y < self._swiat.y:
                    zajete = False
                    for organizm in self._swiat.organizmy:
                        if organizm.polozenie_x == potencjalne_x and organizm.polozenie_y == potencjalne_y:
                            zajete = True
                            break

                    if not zajete:
                        bezpieczne.append(i)

            if bezpieczne:
                wybrany = random.choice(bezpieczne)

                nowe_x = self.polozenie_x + mozliwe_x[wybrany]
                nowe_y = self.polozenie_y + mozliwe_y[wybrany]

                self._stare_polozenie_x = self.polozenie_x
                self._stare_polozenie_y = self.polozenie_y
                self.polozenie_x = nowe_x
                self.polozenie_y = nowe_y

                self._swiat.dodaj_komunikat(f"Umiejetnosc czlowieka ratuje go przed {napastnik.znak}")
                return True

        return False