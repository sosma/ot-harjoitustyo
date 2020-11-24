"""
class for reading words for
"""
class Reader:
    """
    Reader main class
    """
    def __init__(self):
        pass

    def read_from_file(self, path_to_file):
        """
        get data from file
        """
        words = open(path_to_file, "r")
        word_list = []
        for i in words:
            word_list.append(str(i)[:-1].lower())
        return word_list
