from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tavarat = []

    def tavaroita_korissa(self):
        return len(self.tavarat)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.tavarat)

    def lisaa_tuote(self, lisattava: Tuote):
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
