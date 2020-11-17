import re
import itertools
# -*- coding: utf-8 -*-

class WordSnack:
    def __init__(self, words):
        self.words = words
    def get_random_word(self):
        return choice(self.words)
    def find_words(self, letters):
        possible = []
        values = []
        avalible = []
        letters = list(letters)
        data = itertools.permutations(letters)
        for i in data:
            values.append(''.join(i))
        for word in self.words:
            for i in values:
                if word in i:
                    avalible.append(word)
        for word in list(set(avalible)):
            possible.append(word)
        return sorted(possible, key=len)
