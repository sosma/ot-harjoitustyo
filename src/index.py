from ui.ui import UI
from logic.hangman import Hangman
from reader.reader import Reader

RESOURCE = ""
RESOURCE = input("please give the resource file you wish to use:" +\
" (default file src/resources/sanat.txt) ")
if RESOURCE == "":
    RESOURCE =  "src/resources/sanat.txt"
ui = UI(path = RESOURCE)
ui.displayMenu()
