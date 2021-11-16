import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luodun_kassapaatteen_rahat_ja_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    
    def test_kateisella_edullisesti_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.edulliset, 2)

    def test_kateisella_edullisesti_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisella_maukkaasti_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.maukkaat, 2)
    
    def test_kateisella_maukkaasti_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_kortilla_edullisesti_saldo_riittava(self):
        maksukortti = Maksukortti(300)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(maksukortti))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_edullisesti_saldo_ei_riittava(self):
        maksukortti = Maksukortti(200)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(maksukortti))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortilla_maukkaasti_maksu_riittava(self):
        maksukortti = Maksukortti(500)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_maukkaasti_maksu_ei_riittava(self):
        maksukortti = Maksukortti(300)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    

    def test_rahan_lataus_muuttaa_kortin_saldoa_ja_kassan_rahamaaraa(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 300)
        self.assertEqual(str(maksukortti), "saldo: 4.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100300)

    def test_negatiisen_summan_lataus_ei_muuta_mitaan(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -50)
        self.assertEqual(str(maksukortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)