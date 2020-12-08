# pylint: skip-file
import unittest
from reader.reader import Reader
from logic.hangman import Hangman


class TestHangman(unittest.TestCase):
    def setUp(self):
        reader = Reader()
        words = reader.readFromFile("src/resources/sanat.txt")
        self.hangman = Hangman(words)

    def test_finds_correct_word(self):
        result = self.hangman.findWords(4)
        self.assertTrue("talo" in result)
    def test_regex_filters_correctly(self):
        result = self.hangman.findWords(4, "a___")
        self.assertTrue("talo" not in result)
    def test_miss_function_ignores_letters(self):
        self.hangman.miss("a")
        result = self.hangman.findWords(4, "____")
        self.assertTrue("talo" not in result)
    def test_make_reasonable_guess(self):
        words = self.hangman.findWords(5, "k_bab")
        result = self.hangman.guess(words, "k_bab")
        self.assertEqual(result, "e")
    def test_clear_missing(self):
        self.hangman.miss("a")
        self.hangman.reset()
        result = self.hangman.findWords(4)
        self.assertTrue("talo" in result)
