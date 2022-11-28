from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tavarat = []

    def tavaroita_korissa(self):
        return sum(ostos.lukumaara() for ostos in self.tavarat)

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.tavarat)

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.tavarat:
            # Tuotteella ei ole == operaattoria eikä sitä saa muokata
            if ostos.tuote.nimi() == lisattava.nimi() and ostos.tuote.hinta() == lisattava.hinta():
                ostos.muuta_lukumaaraa(1)
                print("Löytyi")
                return

        self.tavarat.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # Bad: kannattaisi palauttaa immutaabeli näkymä listaan, eikä itse listaa.
        return self.tavarat
