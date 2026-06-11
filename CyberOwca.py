from Zwierze import Zwierze

class CyberOwca(Zwierze):
    def __init__(self, polozenie_x, polozenie_y, swiat):
        super().__init__(10, 4, polozenie_x, polozenie_y, swiat, 'Y')

    def rysuj(self):
        self._swiat.narysuj_organizm(self.polozenie_x, self.polozenie_y, 'Y')

    def akcja(self, klawisz=None):
        if self.wiek == 0:
            return

        barszcze = [org for org in self._swiat.organizmy
                    if org.znak == 'B' and org.czy_zyje()]

        if not barszcze:
            super().akcja(klawisz)
            return

        # 3. Znajdujemy najbliższy barszcz za pomocą dystansu Czebyszewa
        # (najlepszy dla ruchu w 8 kierunkach na kracie)
        najblizszy_barszcz = min(barszcze, key=lambda b: max(abs(self.polozenie_x - b.polozenie_x), abs(self.polozenie_y - b.polozenie_y)))

        # 4. Krok w stronę barszczu
        self._stare_polozenie_x = self.polozenie_x
        self._stare_polozenie_y = self.polozenie_y

        dx = najblizszy_barszcz.polozenie_x - self.polozenie_x
        dy = najblizszy_barszcz.polozenie_y - self.polozenie_y

        # Genialny i krótki sposób w Pythonie na wyciągnięcie znaku liczby (-1, 0 lub 1)
        krok_x = (dx > 0) - (dx < 0)
        krok_y = (dy > 0) - (dy < 0)

        nowe_x = self.polozenie_x + krok_x
        nowe_y = self.polozenie_y + krok_y

        # Wykonanie ruchu (jeśli pole nie wychodzi poza mapę)
        if 0 <= nowe_x < self._swiat.x and 0 <= nowe_y < self._swiat.y:
            self.polozenie_x = nowe_x
            self.polozenie_y = nowe_y

    def rozmnazaj(self, x, y):
        return CyberOwca(x, y, self._swiat)