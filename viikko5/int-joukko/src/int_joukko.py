
from copy import copy

KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin tulee olla positiivinen kokonaisluku")

        self.kasvatuskoko = OLETUSKASVATUS if kasvatuskoko is None else kasvatuskoko
        if not isinstance(self.kasvatuskoko, int) or self.kasvatuskoko < 0:
            raise Exception("Kasvatuskoon tulee olla positiivinen kokonaisluku")

        self.alkiot = [0] * kapasiteetti
        self.koko = 0

    def kuuluu(self, luku):
        return luku in self.alkiot[:self.koko]

    def lisaa(self, lisattava_luku):
        self._kasvata_jos_tila_loppu()

        if self.kuuluu(lisattava_luku):
            return False

        self.alkiot[self.koko] = lisattava_luku
        self.koko += 1
        return True

    def _kasvata_jos_tila_loppu(self):
        if self.koko == len(self.alkiot):
            vanhat_alkiot = self.alkiot
            self.alkiot = [0] * (self.koko + self.kasvatuskoko)
            self.alkiot[:self.koko] = vanhat_alkiot

    def poista(self, poistettava_luku):
        for i in range(self.koko):
            if self.alkiot[i] != poistettava_luku:
                continue

            self.alkiot[i:self.koko-1] = self.alkiot[i+1:self.koko]
            self.koko -= 1
            return True

        return False

    def mahtavuus(self):
        return self.koko

    def kopioi_listaksi(self):
        return self.alkiot[:self.koko]

    @staticmethod
    def yhdiste(a, b):
        yhdiste = copy(a)

        for alkio in b:
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()

        for alkio in a:
            if alkio in b:
                leikkaus.lisaa(alkio)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = copy(a)

        for alkio in b:
            erotus.poista(alkio)

        return erotus

    def __getitem__(self, indeksi):
        if indeksi >= self.koko:
            raise IndexError()
        return self.alkiot[indeksi]

    def __len__(self):
        return self.koko

    def __contains__(self, alkio):
        return self.kuuluu(alkio)

    def __str__(self):
        return "{" + ", ".join(str(alkio) for alkio in self.kopioi_listaksi()) + "}"
