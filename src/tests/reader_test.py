# pylint: skip-file
import unittest
from reader import Reader


class TestReader(unittest.TestCase):
    def setUp(self):
        self.reader = Reader()

    def test_read_finnish_words_from_file(self):
        words = self.reader.read_from_file("src/resources/sanat.txt")
        self.assertTrue('makkara' in words)
    def test_changing_word_library(self):
        words = self.reader.read_from_file("src/resources/sanat.txt")
        words = self.reader.read_from_file("src/resources/words.txt")
        self.assertTrue('sausage' in words)
    def test_add_word_to_library(self):
        with open("src/resources/test.txt", "w") as f:
            f.write("")
        self.reader.write_to_file("src/resources/test.txt", "testi")
        words = self.reader.read_from_file("src/resources/test.txt")
        self.assertTrue('testi' in words)
