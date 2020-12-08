"""
class for reading words for
"""
class Reader:
    """
    Reader main class
    """
    def __init__(self):
        pass

    def readFromFile(self, path_to_file):
        """
        get data from file
        """
        words = open(path_to_file, "r")
        word_list = []
        for i in words:
            word_list.append(str(i)[:-1].lower())
        return set(word_list)
    def writeToFile(self, path_to_file, word):
        """
        write a new word to a file
        """
        with open(path_to_file, 'a') as source:
            source.write(word+"\n")