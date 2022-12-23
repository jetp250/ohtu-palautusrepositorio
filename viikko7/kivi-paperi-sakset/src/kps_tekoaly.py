from kivi_sakset_paperi import KiviSaksetPaperi
from tekoaly import Tekoaly

class KPSTekoaly(KiviSaksetPaperi):
    def __init__(self, tekoaly=Tekoaly()):
        self._tekoaly = tekoaly

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
