from ui import UI
from reader import Reader

RESOURCE = input("please give the RESOURCE file you wish to use:" +\
" (default file src/RESOURCEs/sanat.txt) ")
if RESOURCE == "":
    RESOURCE = "src/RESOURCEs/sanat.txt"
add_word = input("if you wish to add a word to the data file please"+ \
"input it now. press enter to continue: ")
if add_word != "":
    if input("are you sure you want to add the word %s to the " + \
    "database, this action cannot be undone? (y/N): " % add_word) == "y":
        reader = Reader()
        reader.write_to_file(RESOURCE, add_word)
ui = UI(path = RESOURCE)
ui.display_menu()
