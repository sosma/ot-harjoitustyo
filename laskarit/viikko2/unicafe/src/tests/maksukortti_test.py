import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_vahennus_toimii(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))

    def test_saldo_ei_mene_negatiiviseksi(self):
        self.assertFalse(self.maksukortti.ota_rahaa(15))

    def test_rahan_lisays_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
