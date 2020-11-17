from hangman import Hangman
from word_snack import WordSnack
from reader import Reader

reader = Reader()
words = reader.read_from_file("src/resources/sanat.txt")
word_snack = WordSnack(words)
print(word_snack.find_words('norsu'))
