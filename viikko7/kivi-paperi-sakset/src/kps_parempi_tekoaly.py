from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self, muistin_koko = 10):
        super().__init__(TekoalyParannettu(muistin_koko))

    def _toisen_siirto(self, ensimmaisen_siirto):
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return super()._toisen_siirto(ensimmaisen_siirto)
