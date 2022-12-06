
from sovelluslogiikka import Sovelluslogiikka

class Kumottava:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self.edellinen = None

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._vanha_arvo)

    def suorita(self):
        self._vanha_arvo = self._sovelluslogiikka.tulos

class Summa(Kumottava):
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka)
        self._lue_syote = lue_syote

    def suorita(self):
        super().suorita()
        luku = self._lue_syote()
        self._sovelluslogiikka.plus(luku)


class Erotus(Kumottava):
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka)
        self._lue_syote = lue_syote

    def suorita(self):
        super().suorita()
        luku = self._lue_syote()
        self._sovelluslogiikka.miinus(luku)

class Nollaus(Kumottava):
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        super().__init__(sovelluslogiikka)
    
    def suorita(self):
        super().suorita()
        self._sovelluslogiikka.nollaa()
