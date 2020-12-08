
"""
word snack logic engine
"""
import itertools
# -*- coding: utf-8 -*-

class WordSnack:
    """
    word snack main class
    """
    def __init__(self, words):
        self.words = words
    def findWords(self, letters):
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
            if len(word) <= 1:
                continue
            possible.append(word)
        return sorted(possible, key=len)
