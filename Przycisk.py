import pygame

class Przycisk:
    def __init__(self, x, y, szerokosc, wysokosc, tekst, kolor_podstawowy, kolor_hover):
        self.prostokat = pygame.Rect(x, y, szerokosc, wysokosc)
        self.tekst = tekst
        self.kolor_podstawowy = kolor_podstawowy
        self.kolor_hover = kolor_hover
        self.czcionka = pygame.font.SysFont('arial', 20, bold=True)

    def rysuj(self, okno, pozycja_myszy):
        if self.prostokat.collidepoint(pozycja_myszy):
            pygame.draw.rect(okno, self.kolor_hover, self.prostokat)
        else:
            pygame.draw.rect(okno, self.kolor_podstawowy, self.prostokat)
        pygame.draw.rect(okno, (0, 0, 0), self.prostokat, 2)

        tekst_obraz = self.czcionka.render(self.tekst, True, (0, 0, 0))
        tekst_pozycja = tekst_obraz.get_rect(center=self.prostokat.center)
        okno.blit(tekst_obraz, tekst_pozycja)

    def sprawdz_klikniecie(self, pozycja_myszy):
        return self.prostokat.collidepoint(pozycja_myszy)
