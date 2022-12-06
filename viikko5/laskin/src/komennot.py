
from sovelluslogiikka import Sovelluslogiikka


class Summa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        luku = self._lue_syote()
        self._sovelluslogiikka.plus(luku)


class Erotus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        luku = self._lue_syote()
        self._sovelluslogiikka.miinus(luku)

class Nollaus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        pass