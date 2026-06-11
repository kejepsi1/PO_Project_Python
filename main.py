import pygame
import sys

from Swiat import Swiat
from Czlowiek import Czlowiek
from Wilk import Wilk
from Owca import Owca
from Lis import Lis
from Zolw import Zolw
from Antylopa import Antylopa
from Trawa import Trawa
from Mlecz import Mlecz
from Guarana import Guarana
from WilczeJagody import WilczeJagody
from BarszczSosnowskiego import BarszczSosnowskiego

# --- USTAWIENIA WIZUALNE ---
ROZMIAR_POLA = 30
SZEROKOSC_SIATKI = 20
WYSOKOSC_SIATKI = 20
SZEROKOSC_UI = 350  # Szerokość bocznego panelu na interfejs

KOLOR_TLA_PLANSZY = (200, 200, 200)
KOLOR_TLA_UI = (50, 50, 50)
KOLOR_TEKSTU_UI = (255, 255, 255)


class Przycisk:
    def __init__(self, x, y, szerokosc, wysokosc, tekst, kolor_podstawowy, kolor_hover):
        self.prostokat = pygame.Rect(x, y, szerokosc, wysokosc)
        self.tekst = tekst
        self.kolor_podstawowy = kolor_podstawowy
        self.kolor_hover = kolor_hover
        self.czcionka = pygame.font.SysFont('arial', 20, bold=True)

    def rysuj(self, okno, pozycja_myszy):
        # Zmiana koloru, gdy myszka najedzie na przycisk
        if self.prostokat.collidepoint(pozycja_myszy):
            pygame.draw.rect(okno, self.kolor_hover, self.prostokat)
        else:
            pygame.draw.rect(okno, self.kolor_podstawowy, self.prostokat)

        # Obramowanie
        pygame.draw.rect(okno, (0, 0, 0), self.prostokat, 2)

        # Centrowanie tekstu na przycisku
        tekst_obraz = self.czcionka.render(self.tekst, True, (0, 0, 0))
        tekst_pozycja = tekst_obraz.get_rect(center=self.prostokat.center)
        okno.blit(tekst_obraz, tekst_pozycja)

    def sprawdz_klikniecie(self, pozycja_myszy):
        return self.prostokat.collidepoint(pozycja_myszy)


def rysuj_interfejs(okno, swiat, przyciski, czcionka_ui):
    # Rysowanie tła pod UI
    panel_ui = pygame.Rect(SZEROKOSC_SIATKI * ROZMIAR_POLA, 0, SZEROKOSC_UI, WYSOKOSC_SIATKI * ROZMIAR_POLA)
    pygame.draw.rect(okno, KOLOR_TLA_UI, panel_ui)

    # 1. Dane Autora (Wymóg z PDF!)
    autor_tekst = czcionka_ui.render("Mikołaj Tchorek, 208435", True, KOLOR_TEKSTU_UI)
    okno.blit(autor_tekst, (SZEROKOSC_SIATKI * ROZMIAR_POLA + 20, 20))

    # 2. Rysowanie przycisków
    pozycja_myszy = pygame.mouse.get_pos()
    for przycisk in przyciski:
        przycisk.rysuj(okno, pozycja_myszy)

    # 3. Rysowanie komunikatów (Log zdarzeń)
    naglowek_komunikatow = czcionka_ui.render("Krótka historia zdarzeń:", True, (200, 200, 0))
    okno.blit(naglowek_komunikatow, (SZEROKOSC_SIATKI * ROZMIAR_POLA + 20, 270))

    czcionka_logu = pygame.font.SysFont('arial', 14)
    # Pobieramy tylko 15 ostatnich wiadomości, żeby nie wyjść poza ekran
    ostatnie_komunikaty = swiat.komunikaty[-15:]

    y_komunikatu = 300
    for wiadomosc in ostatnie_komunikaty:
        tekst_obraz = czcionka_logu.render(wiadomosc, True, KOLOR_TEKSTU_UI)
        okno.blit(tekst_obraz, (SZEROKOSC_SIATKI * ROZMIAR_POLA + 20, y_komunikatu))
        y_komunikatu += 18  # Odstęp między linijkami


def main():
    pygame.init()

    # Tworzymy okno powiększone o szerokość interfejsu (UI)
    szerokosc_okna = SZEROKOSC_SIATKI * ROZMIAR_POLA + SZEROKOSC_UI
    wysokosc_okna = WYSOKOSC_SIATKI * ROZMIAR_POLA
    okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
    pygame.display.set_caption("Wirtualny Świat - Symulacja")

    czcionka_ui = pygame.font.SysFont('arial', 20, bold=True)

    swiat = Swiat(SZEROKOSC_SIATKI, WYSOKOSC_SIATKI)

    # Inicjalizacja przycisków
    poczatek_ui_x = SZEROKOSC_SIATKI * ROZMIAR_POLA + 25
    przycisk_tura = Przycisk(poczatek_ui_x, 70, 300, 40, "Następna Tura", (100, 200, 100), (150, 250, 150))
    przycisk_zapisz = Przycisk(poczatek_ui_x, 130, 300, 40, "Zapisz Grę", (100, 150, 200), (150, 200, 250))
    przycisk_wczytaj = Przycisk(poczatek_ui_x, 190, 300, 40, "Wczytaj Grę", (200, 150, 100), (250, 200, 150))

    przyciski = [przycisk_tura, przycisk_zapisz, przycisk_wczytaj]

    dziala = True

    while dziala:
        wcisniety_klawisz = None
        pozycja_myszy = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dziala = False

            # OBSŁUGA KLAWIATURY (Ruch człowieka)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    wcisniety_klawisz = 'UP'
                elif event.key == pygame.K_DOWN:
                    wcisniety_klawisz = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    wcisniety_klawisz = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    wcisniety_klawisz = 'RIGHT'
                elif event.key == pygame.K_SPACE:
                    wcisniety_klawisz = 'SPACE'

                # Jeśli wciśnięto przycisk ruchu, wykonujemy turę z klawiszem
                if wcisniety_klawisz:
                    swiat.wykonaj_ture(wcisniety_klawisz)

            # OBSŁUGA MYSZKI (Klikanie w przyciski i planszę)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 to Lewy Przycisk Myszy (LPM)
                    # 1. Czy kliknięto któryś z przycisków?
                    if przycisk_tura.sprawdz_klikniecie(pozycja_myszy):
                        swiat.wykonaj_ture()  # Tura bez klawisza (człowiek stoi)
                    elif przycisk_zapisz.sprawdz_klikniecie(pozycja_myszy):
                        swiat.zapisz_do_pliku()
                    elif przycisk_wczytaj.sprawdz_klikniecie(pozycja_myszy):
                        swiat.wczytaj_z_pliku()

                    # 2. Czy kliknięto na siatkę gry (planszę)?
                    elif pozycja_myszy[0] < SZEROKOSC_SIATKI * ROZMIAR_POLA:
                        x_kliku_na_siatce = pozycja_myszy[0] // ROZMIAR_POLA
                        y_kliku_na_siatce = pozycja_myszy[1] // ROZMIAR_POLA
                        # TODO: Wyświetlić menu dodawania organizmu w tym miejscu!
                        print(f"Kliknięto pole: {x_kliku_na_siatce}, {y_kliku_na_siatce}")

        # --- RENDEROWANIE ---
        okno.fill(KOLOR_TLA_PLANSZY)

        # 1. Rysowanie świata (siatka i organizmy)
        swiat.rysuj(okno, ROZMIAR_POLA)

        # 2. Rysowanie interfejsu (przyciski, logi)
        rysuj_interfejs(okno, swiat, przyciski, czcionka_ui)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()