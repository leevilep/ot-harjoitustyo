import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataus_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(300)
        self.assertEqual(str(self.maksukortti), "saldo: 13.0")

    def test_saldo_vahenee_jos_rahaa_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(400))
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertTrue(self.maksukortti.ota_rahaa(600))
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_saldo_ei_vahene_jos_rahaa_ei_tarpeeksi(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1200))
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")