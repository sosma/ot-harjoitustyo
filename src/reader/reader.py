"""
class for reading words for
"""
class Reader:
    """
    Reader main class
    """
    def __init__(self):
        pass

    def readFromFile(self, pathToFile):
        """
        get data from file
        """
        words = open(pathToFile, "r")
        wordList = []
        for i in words:
            wordList.append(str(i)[:-1].lower())
        return set(wordList)
    def writeToFile(self, pathToFile, word):
        """
        write a new word to a file
        """
        with open(pathToFile, 'a') as source:
            source.write(word+"\n")
