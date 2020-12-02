from random import choice
class Hangman:
    def __init__(self, words):
        self.words = words
        self.alphabet = set([c for word in words for c in word if c is not " "])
    def get_random_word(self):
        """
        method for getting a random word
        """
        return choice(self.words)
    def guess_word(self, lenght):
        """
        method for guessing a word from given letters
        """
        pass
