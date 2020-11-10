import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(400)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.kortti), "saldo: 4.0")

    def test_lataa_kortille_rahaa_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 69)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100069)
        self.assertEqual(str(self.kortti), "saldo: 4.69")

    def test_konstruktori_asettaa_arvot_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myy_edullinen_kortilla_jos_tarpeeksi_rahaa(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))
        self.assertTrue(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_ala_myy_edullinen_kortilla_jos_ei_tarpeeksi_rahaa(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti))
        self.assertTrue(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_myy_maukas_kortilla_jos_tarpeeksi_rahaa(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))
        self.assertTrue(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_ala_myy_maukas_kortilla_jos_ei_tarpeeksi_rahaa(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))
        self.assertTrue(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_myy_edullinen_kateisellla_jos_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertTrue(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_ala_myy_edullinen_kateisellla_jos_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertTrue(self.kassapaate.kassassa_rahaa, 10000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myy_maukas_kateisellla_jos_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertTrue(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_ala_myy_maukas_kateisellla_jos_ei_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(123)
        self.assertTrue(self.kassapaate.kassassa_rahaa, 10000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_vaihtoraha_oikein_kun_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)

    def test_syo_edullisesti_kateisella_vaihtoraha_oikein_kun_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(239), 239)

    def test_syo_maukkaasti_kateisella_vaihtoraha_oikein_kun_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)

    def test_syo_maukkaasti_kateisella_vaihtoraha_oikein_kun_ei_tarpeeksi_rahaa(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(123), 123)

    # def test_saldo_ei_mene_negatiiviseksi(self):
    #     self.assertFalse(self.maksukortti.ota_rahaa(15))
    #
    # def test_rahan_lisays_toimii(self):
    #     self.maksukortti.lataa_rahaa(10)
    #     self.assertEqual(str(self.maksukortti), "saldo: 0.2")
