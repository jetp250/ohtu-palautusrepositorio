import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.varasto_mock = Mock()

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_kahden_eri_tuotteen_osto_tuottaa_oikean_tilisiirron(self):
        self.viitegeneraattori_mock.uusi.return_value = 43

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "tomaatti", 2)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("matti", "23456")

        self.pankki_mock.tilisiirto.assert_called_with("matti", 43, "23456", "33333-44455", 5+2)

    def test_kahden_saman_tuotteen_osto_tuottaa_oikean_tilisiirron(self):
        self.viitegeneraattori_mock.uusi.return_value = 43

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "23456")

        self.pankki_mock.tilisiirto.assert_called_with("matti", 43, "23456", "33333-44455", 5+5)

    def test_loppuneesta_tuotteesta_ei_veloiteta(self):
        self.viitegeneraattori_mock.uusi.return_value = 43

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("matti", "23456")

        self.pankki_mock.tilisiirto.assert_called_with("matti", 43, "23456", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_tiedot(self):
        self.viitegeneraattori_mock.uusi.return_value = 43

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "23456")
        self.pankki_mock.tilisiirto.assert_called_with("matti", 43, "23456", "33333-44455", 5)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "23456")
        self.pankki_mock.tilisiirto.assert_called_with("matti", 43, "23456", "33333-44455", 5)

    def test_jokaiselle_maksutapahtumalle_generoidaan_viite(self):
        self.viitegeneraattori_mock.uusi.return_value = 43

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "23456")
        self.viitegeneraattori_mock.uusi.assert_called()

        self.viitegeneraattori_mock.uusi.called = False

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("matti", "23456")
        self.viitegeneraattori_mock.uusi.assert_called()

    def test_ostoskorista_poistetusta_tuotteesta_ei_veloiteta(self):
        self.viitegeneraattori_mock.uusi.return_value = 43

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "tomaatti", 2)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.poista_korista(1)
        kauppa.tilimaksu("matti", "23456")
        self.pankki_mock.tilisiirto.assert_called_with("matti", 43, "23456", "33333-44455", 2)