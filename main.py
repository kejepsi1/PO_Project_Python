import pygame
import sys

from CyberOwca import CyberOwca
from Swiat import Swiat
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
from Przycisk import Przycisk

ROZMIAR_POLA = 30
SZEROKOSC_SIATKI = 20
WYSOKOSC_SIATKI = 20
SZEROKOSC_UI = 350

KOLOR_TLA_PLANSZY = (200, 200, 200)
KOLOR_TLA_UI = (50, 50, 50)
KOLOR_TEKSTU_UI = (255, 255, 255)

def rysuj_interfejs(okno, swiat, przyciski, czcionka_ui):
    panel_ui = pygame.Rect(SZEROKOSC_SIATKI * ROZMIAR_POLA, 0, SZEROKOSC_UI, WYSOKOSC_SIATKI * ROZMIAR_POLA)
    pygame.draw.rect(okno, KOLOR_TLA_UI, panel_ui)

    autor_tekst = czcionka_ui.render("Mikołaj Tchorek, 208435", True, KOLOR_TEKSTU_UI)
    okno.blit(autor_tekst, (SZEROKOSC_SIATKI * ROZMIAR_POLA + 20, 20))

    pozycja_myszy = pygame.mouse.get_pos()
    for przycisk in przyciski:
        przycisk.rysuj(okno, pozycja_myszy)

    naglowek_komunikatow = czcionka_ui.render("Komunikaty:", True, (200, 200, 0))
    okno.blit(naglowek_komunikatow, (SZEROKOSC_SIATKI * ROZMIAR_POLA + 20, 270))

    czcionka_logu = pygame.font.SysFont('arial', 14)
    ostatnie_komunikaty = swiat.komunikaty[-15:]

    y_komunikatu = 300
    for wiadomosc in ostatnie_komunikaty:
        tekst_obraz = czcionka_logu.render(wiadomosc, True, KOLOR_TEKSTU_UI)
        okno.blit(tekst_obraz, (SZEROKOSC_SIATKI * ROZMIAR_POLA + 20, y_komunikatu))
        y_komunikatu += 18


def main():
    pygame.init()

    szerokosc_okna = SZEROKOSC_SIATKI * ROZMIAR_POLA + SZEROKOSC_UI
    wysokosc_okna = WYSOKOSC_SIATKI * ROZMIAR_POLA
    okno = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
    pygame.display.set_caption("Wirtualny Świat")

    czcionka_ui = pygame.font.SysFont('arial', 20, bold=True)
    czcionka_menu = pygame.font.SysFont('arial', 14)

    swiat = Swiat(SZEROKOSC_SIATKI, WYSOKOSC_SIATKI)

    poczatek_ui_x = SZEROKOSC_SIATKI * ROZMIAR_POLA + 25
    przycisk_tura = Przycisk(poczatek_ui_x, 70, 300, 40, "Następna Tura", (100, 200, 100), (150, 250, 150))
    przycisk_zapisz = Przycisk(poczatek_ui_x, 130, 300, 40, "Zapisz Grę", (100, 150, 200), (150, 200, 250))
    przycisk_wczytaj = Przycisk(poczatek_ui_x, 190, 300, 40, "Wczytaj Grę", (200, 150, 100), (250, 200, 150))
    przyciski = [przycisk_tura, przycisk_zapisz, przycisk_wczytaj]

    menu_aktywne = False
    wybrane_pole_x = 0
    wybrane_pole_y = 0
    menu_rects = []

    lista_gatunkow = [
        ("Wilk", Wilk), ("Owca", Owca), ("Lis", Lis), ("Żółw", Zolw),
        ("Antylopa", Antylopa),("CyberOwca", CyberOwca), ("Trawa", Trawa), ("Mlecz", Mlecz),
        ("Guarana", Guarana), ("Wilcze Jagody", WilczeJagody),
        ("Barszcz Sosnowskiego", BarszczSosnowskiego)
    ]

    dziala = True

    while dziala:
        wcisniety_klawisz = None
        pozycja_myszy = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dziala = False

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
                elif event.key == pygame.K_w:
                    wcisniety_klawisz = 'W'
                elif event.key == pygame.K_r:
                    wcisniety_klawisz = 'R'
                elif event.key == pygame.K_x:
                    wcisniety_klawisz = 'X'
                elif event.key == pygame.K_v:
                    wcisniety_klawisz = 'V'


                if wcisniety_klawisz and not menu_aktywne:
                    swiat.wykonaj_ture(wcisniety_klawisz)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if menu_aktywne:
                        for rect, Klasa, nazwa in menu_rects:
                            if rect.collidepoint(pozycja_myszy):
                                nowy_organizm = Klasa(wybrane_pole_x, wybrane_pole_y, swiat)
                                swiat.dodaj_organizm(nowy_organizm)
                                swiat.dodaj_komunikat(f"Dodano ręcznie: {nazwa}")
                                break

                        menu_aktywne = False
                    else:
                        if przycisk_tura.sprawdz_klikniecie(pozycja_myszy):
                            swiat.wykonaj_ture()
                        elif przycisk_zapisz.sprawdz_klikniecie(pozycja_myszy):
                            swiat.zapisz_do_pliku()
                        elif przycisk_wczytaj.sprawdz_klikniecie(pozycja_myszy):
                            swiat.wczytaj_z_pliku()

                        elif pozycja_myszy[0] < SZEROKOSC_SIATKI * ROZMIAR_POLA:
                            x_kliku = pozycja_myszy[0] // ROZMIAR_POLA
                            y_kliku = pozycja_myszy[1] // ROZMIAR_POLA

                            zajete = any(org.polozenie_x == x_kliku and org.polozenie_y == y_kliku and org.czy_zyje() for org in swiat.organizmy)

                            if not zajete:
                                menu_aktywne = True
                                wybrane_pole_x = x_kliku
                                wybrane_pole_y = y_kliku

                                menu_rects.clear()
                                menu_x = pozycja_myszy[0]
                                menu_y = pozycja_myszy[1]
                                szer_menu = 160
                                wys_opcji = 25

                                if menu_y + len(lista_gatunkow) * wys_opcji > wysokosc_okna:
                                    menu_y = wysokosc_okna - len(lista_gatunkow) * wys_opcji

                                for i, (nazwa, Klasa) in enumerate(lista_gatunkow):
                                    rect = pygame.Rect(menu_x, menu_y + i * wys_opcji, szer_menu, wys_opcji)
                                    menu_rects.append((rect, Klasa, nazwa))

        okno.fill(KOLOR_TLA_PLANSZY)

        swiat.rysuj(okno, ROZMIAR_POLA)
        rysuj_interfejs(okno, swiat, przyciski, czcionka_ui)

        if menu_aktywne:
            for rect, _, nazwa in menu_rects:
                kolor_tla = (180, 200, 255) if rect.collidepoint(pozycja_myszy) else (230, 230, 230)
                pygame.draw.rect(okno, kolor_tla, rect)
                pygame.draw.rect(okno, (0, 0, 0), rect, 1)  # Ramka

                tekst = czcionka_menu.render(nazwa, True, (0, 0, 0))
                okno.blit(tekst, (rect.x + 5, rect.y + 3))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()