"""
class for reading words for
"""
class Reader:
    def __init__(self):
        pass
    def read_from_file(self, path_to_file):
        words = open(path_to_file, "r")
        ls = []
        for i in words:
            ls.append(str(i)[:-1].lower())
        return ls
