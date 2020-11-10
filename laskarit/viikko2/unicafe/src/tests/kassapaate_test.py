import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def alustus_oikein(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.maukkaat, 0)

    def test_edullisen_kateisosto(self):
        self.assertEqual(self.paate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.paate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.paate.kassassa_rahaa, 100240)
        self.assertEqual(self.paate.edulliset, 1)

    def test_maukkaan_kateisosto(self):
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
        self.assertEqual(self.paate.maukkaat, 0)
        self.assertEqual(self.paate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.paate.kassassa_rahaa, 100400)
        self.assertEqual(self.paate.maukkaat, 1)

# Valitettavasti jaa kesken etta ehtii pushaamaan dedikseen mennessa
"""
    def test_edullisen_korttiosto(self):
        for i in range(4):
            assert self.paate.syo_edullisesti_kortilla(self.kortti)
            self.assertEqual(self.kortti.saldo, 10000 - i*240)
            self.assertEqual(self.edulliset, i)
        assert not self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 10000 - 4*240)
        self.assertEqual(self.edulliset, 4)
"""