# pylint: skip-file
import unittest
from reader import Reader
from word_snack import WordSnack


class TestWordSnack(unittest.TestCase):
    def setUp(self):
        reader = Reader()
        words = reader.readFromFile("src/resources/sanat.txt")
        self.word_snack = WordSnack(words)

    def test_find_correct_word(self):
        words = self.word_snack.findWords('keba')
        self.assertTrue('eka' in words)

    def test_dont_find_incorrect_word(self):
        words = self.word_snack.findWords('keba')
        self.assertFalse('kebab' in words)
