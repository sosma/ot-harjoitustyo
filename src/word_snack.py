import itertools
# -*- coding: utf-8 -*-

"""
Class for solving word snack problems
"""
class WordSnack:
    """
    word snack main class
    """
    def __init__(self, words):
        self.words = words
    def find_words(self, letters):
        """
        get possible words from letters
        """
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
