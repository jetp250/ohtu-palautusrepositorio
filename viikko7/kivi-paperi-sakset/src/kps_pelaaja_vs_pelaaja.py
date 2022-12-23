from kivi_sakset_paperi import KiviSaksetPaperi

class KPSPelaajaVsPelaaja(KiviSaksetPaperi):
    def _toisen_siirto(self, ensimmaisen_siirto):
        return input("Toisen pelaajan siirto: ")

