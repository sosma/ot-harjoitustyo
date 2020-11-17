import unittest
from reader import Reader
from word_snack import WordSnack


class TestWordSnack(unittest.TestCase):
    def setUp(self):
        reader = Reader()
        words = reader.read_from_file("src/resources/sanat.txt")
        self.word_snack = WordSnack(words)

    def test_find_correct_word(self):
        words = self.word_snack.find_words('keba')
        self.assertTrue('eka' in words)

    def test_dont_find_incorrect_word(self):
        words = self.word_snack.find_words('keba')
        self.assertFalse('kebab' in words)
