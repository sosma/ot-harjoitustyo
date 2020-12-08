from ui.ui import UI
from logic.hangman import Hangman
from data_managament.reader import Reader

RESOURCE = ""
RESOURCE = input("please give the resource file you wish to use:" +\
" (default file src/resources/sanat.txt) ")
if RESOURCE == "":
    RESOURCE = "src/resources/sanat.txt"
addWord = input("if you wish to add a word to the data file please "+ \
"input it now. press enter to continue: ")
if addWord != "":
    if input("are you sure you want to add the word %s to the " + \
    "database, this action cannot be undone? (y/N): " % addWord) == "y":
        reader = Reader()
        reader.write_to_file(RESOURCE, addWord)
ui = UI(path = RESOURCE)
ui.display_menu()
