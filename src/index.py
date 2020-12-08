"""
starts the word helper program
"""
from ui.ui import UI

RESOURCE = ""
RESOURCE = input("please give the resource file you wish to use:" +\
" (default file src/resources/sanat.txt) ")
if RESOURCE == "":
    RESOURCE =  "src/resources/sanat.txt"
ui = UI(path = RESOURCE)
ui.displayMenu()
