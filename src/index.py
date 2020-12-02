from ui import UI
from reader import Reader

resource = input("please give the resource file you wish to use: (default file src/resources/sanat.txt) ")
if resource == "": resource = "src/resources/sanat.txt"
add_word = input("if you wish to add a word to the data file please input it now. press enter to continue: ")
if add_word != "":
    if input("are you sure you want to add the word %s to the database, this action cannot be undone? (y/N): " % add_word) == "y":
        reader = Reader()
        reader.write_to_file(resource, add_word)
ui = UI(path = resource)
ui.display_menu()
