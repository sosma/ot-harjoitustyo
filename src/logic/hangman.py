"""
Hangman logic engine
"""
import re
import operator

# -*- coding: utf-8 -*-


class Hangman:
    """
    Hangman game object
    """
    def __init__(self, words):
        self.words = words
        self.alphabet = set([c for word in words for c in word if c is not " "])
        self.missed=""
    def findWords(self, lenght, current=""):
        """
        select correct length words
        """
        words = [x for x in self.words if len(x) == lenght]
        wordsTmp = []
        if current!="":
            regexString = current.replace("_", ".")
            for word in words:
                if re.match(regexString, word):
                    addWord = True
                    for letter in word:
                        if letter in self.missed:
                            addWord = False
                    if addWord:
                        wordsTmp.append(word)
            words = wordsTmp
        return words
    def guess(self, words, current):
        """
        check witch letter covers most of the unguessed words and propose that as a guess
        """
        results = {}
        emptyIndeces = []
        for i in range(len(current)):
            if current[i] == "_":
                emptyIndeces.append(i)
        for letter in self.alphabet:
            results[letter] = 0
        for word in words:
            missingLetters = []
            for index in emptyIndeces:
                missingLetters.append(word[index])
            for letter in self.alphabet:
                if letter in missingLetters and letter not in current:
                    results[letter] += 1
        return max(results.items(), key=operator.itemgetter(1))[0]
    def miss(self, letter):
        """
        note that a letter did not fit the word
        """
        self.missed+=letter
    def reset(self):
        """
        clear missed letters
        """
        self.missed = ""
