from random import choice
class Hangman:
    def __init__(self, words):
        self.words = words
        self.alphabet = set([c for word in words for c in word if c is not " "])
    def get_random_word(self):
        return choice(self.words)
    def guess_word(self, lenght):
        pass
