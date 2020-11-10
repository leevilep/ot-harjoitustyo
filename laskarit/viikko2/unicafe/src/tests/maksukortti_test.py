import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.00")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1234)
        self.assertEqual(str(self.maksukortti), "saldo: 22.34")
        self.maksukortti.lataa_rahaa(0)
        self.assertEqual(str(self.maksukortti), "saldo: 22.34")
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 22.44")
        
    def test_rahan_ottaminen_toimii_oikein(self):
        #tarpeeksi rahaa
        assert self.maksukortti.ota_rahaa(800)
        self.assertEqual(str(self.maksukortti), "saldo: 2.00")
        
        #ei enää tarpeeksi rahaa
        assert not self.maksukortti.ota_rahaa(800)
        self.assertEqual(str(self.maksukortti), "saldo: 2.00")
        

