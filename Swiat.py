import random
import pygame
import json
import os

from CyberOwca import CyberOwca
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


class Swiat:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.komunikaty = []
        self.organizmy = []

        self.dodaj_bezpiecznie_organizm(Czlowiek(0, 0, self))
        for _ in range(5):
            self.dodaj_bezpiecznie_organizm(Wilk(0, 0, self))
            self.dodaj_bezpiecznie_organizm(Trawa(0, 0, self))
            self.dodaj_bezpiecznie_organizm(Owca(0, 0, self))
            self.dodaj_bezpiecznie_organizm(Mlecz(0, 0, self))
            self.dodaj_bezpiecznie_organizm(Lis(0, 0, self))
            self.dodaj_bezpiecznie_organizm(Zolw(0, 0, self))
            self.dodaj_bezpiecznie_organizm(Antylopa(0, 0, self))
            self.dodaj_bezpiecznie_organizm(Guarana(0, 0, self))
            self.dodaj_bezpiecznie_organizm(WilczeJagody(0, 0, self))
            self.dodaj_bezpiecznie_organizm(BarszczSosnowskiego(0, 0, self))
            self.dodaj_bezpiecznie_organizm(CyberOwca(0,0,self))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def dodaj_wiek(self):
        for organizm in self.organizmy:
            organizm.wiek += 1

    def dodaj_komunikat(self, komunikat):
        self.komunikaty.append(komunikat)

    def dodaj_bezpiecznie_organizm(self, organizm):
        if len(self.organizmy) >= self._x * self._y:
            return

        zajete = True
        while zajete:
            zajete = False
            rand_x = random.randint(0, self._x - 1)
            rand_y = random.randint(0, self._y - 1)

            for org in self.organizmy:
                if org.polozenie_x == rand_x and org.polozenie_y == rand_y:
                    zajete = True
                    break

        organizm.polozenie_x = rand_x
        organizm.polozenie_y = rand_y
        self.dodaj_organizm(organizm)

    def dodaj_organizm(self, organizm):
        if organizm is not None:
            self.organizmy.append(organizm)

    def sprawdzaj_kolizje(self, napastnik):
        for obronca in self.organizmy:
            if obronca is napastnik or not obronca.czy_zyje() or not napastnik.czy_zyje():
                continue

            if obronca.polozenie_x == napastnik.polozenie_x and obronca.polozenie_y == napastnik.polozenie_y:
                if obronca.czy_mozna_zdeptac(napastnik):
                    continue

                if obronca.znak == napastnik.znak:
                    napastnik.cofnij()
                    obronca.rozmnoz_sie()
                    return

                if not obronca.czy_odpycha(napastnik):
                    if not obronca.czy_obronil(napastnik):
                        if obronca.uniknij_smierci(napastnik):
                            return

                        self.dodaj_komunikat(f"{napastnik.znak} zjada {obronca.znak}")
                        obronca.zabij()
                        return
                    else:
                        if napastnik.uniknij_smierci(obronca):
                            return

                        self.dodaj_komunikat(f"{obronca.znak} zjada {napastnik.znak}")
                        napastnik.zabij()
                        return
                else:
                    return

    def wykonaj_ture(self, wcisniety_klawisz=None):
        self.organizmy.sort(key=lambda org: (-org.inicjatywa, -org.wiek))

        self.komunikaty.clear()

        for organizm in list(self.organizmy):
            if organizm.czy_zyje():
                organizm.akcja(wcisniety_klawisz)
                organizm.kolizja()

        self.organizmy = [org for org in self.organizmy if org.czy_zyje()]
        self.dodaj_wiek()

    def rysuj(self, okno, rozmiar_pola):
        for x in range(self._x):
            for y in range(self._y):
                prostokat = pygame.Rect(x * rozmiar_pola, y * rozmiar_pola, rozmiar_pola, rozmiar_pola)
                pygame.draw.rect(okno, (150, 150, 150), prostokat, 1)

        czcionka = pygame.font.SysFont('arial', int(rozmiar_pola * 0.6), bold=True)
        kolory = {
            'C': (0, 0, 255),
            'W': (128, 128, 128),
            'O': (255, 255, 255),
            'L': (255, 165, 0),
            'Z': (0, 100, 0),
            'A': (139, 69, 19),
            'T': (124, 252, 0),
            'M': (255, 255, 0),
            'G': (255, 0, 0),
            'J': (128, 0, 128),
            'B': (0, 0, 0),
            'Y': (0,255,255)
        }

        for organizm in reversed(self.organizmy):
            if organizm.czy_zyje():
                x_piksele = organizm.polozenie_x * rozmiar_pola
                y_piksele = organizm.polozenie_y * rozmiar_pola

                kolor = kolory.get(organizm.znak, (50, 50, 50))

                kwadrat = pygame.Rect(x_piksele, y_piksele, rozmiar_pola, rozmiar_pola)
                pygame.draw.rect(okno, kolor, kwadrat)

                kolor_tekstu = (255, 255, 255) if organizm.znak in ['B', 'J'] else (0, 0, 0)

                tekst_obraz = czcionka.render(organizm.znak, True, kolor_tekstu)

                tekst_pozycja = tekst_obraz.get_rect(center=kwadrat.center)

                okno.blit(tekst_obraz, tekst_pozycja)


    def zapisz_do_pliku(self, nazwa_pliku="zapis_gry.json"):
        dane_swiata = {
            "wymiarX": self._x,
            "wymiarY": self._y,
            "listaOrganizmow": []
        }

        for org in self.organizmy:
            dane_org = {
                "znak": org.znak,
                "x": org.polozenie_x,
                "y": org.polozenie_y,
                "sila": org.sila,
                "wiek": org.wiek
            }
            if isinstance(org, Czlowiek):
                dane_org["trwanieUmiejetnosci"] = org.czas_trwania_umiejetnosci
                dane_org["odnowienieUmiejetnosci"] = org.czas_odnowienia_umiejetnosci

            dane_swiata["listaOrganizmow"].append(dane_org)

        try:
            with open(nazwa_pliku, 'w') as plik:
                json.dump(dane_swiata, plik, indent=4)
            self.dodaj_komunikat("Gra zostala zapisana do pliku.")
        except IOError as e:
            print(f"Błąd zapisu: {e}")

    def wczytaj_z_pliku(self, nazwa_pliku="zapis_gry.json"):
        if not os.path.exists(nazwa_pliku):
            print("Brak pliku zapisu!")
            return

        try:
            with open(nazwa_pliku, 'r') as plik:
                dane_swiata = json.load(plik)

            self._x = dane_swiata.get("wymiarX", 20)
            self._y = dane_swiata.get("wymiarY", 20)
            self.organizmy.clear()
            self.komunikaty.clear()

            klasy_organizmow = {
                'C': Czlowiek, 'W': Wilk, 'O': Owca, 'L': Lis,
                'Z': Zolw, 'A': Antylopa, 'Y': CyberOwca, 'T': Trawa, 'M': Mlecz,
                'G': Guarana, 'J': WilczeJagody, 'B': BarszczSosnowskiego
            }

            for dane_org in dane_swiata.get("listaOrganizmow", []):
                znak = dane_org["znak"]
                Klasa = klasy_organizmow.get(znak)

                if Klasa:
                    nowy = Klasa(dane_org["x"], dane_org["y"], self)
                    nowy.sila = dane_org["sila"]
                    nowy.wiek = dane_org["wiek"]

                    if znak == 'C':
                        nowy.czas_trwania_umiejetnosci = dane_org.get("trwanieUmiejetnosci", 0)
                        nowy.czas_odnowienia_umiejetnosci = dane_org.get("odnowienieUmiejetnosci", 0)

                    self.organizmy.append(nowy)

            self.dodaj_komunikat("Wczytano zapisana gre!")
        except Exception as e:
            print(f"Blad podczas wczytywania: {e}")