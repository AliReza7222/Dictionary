# This file menu.py is for test because this project run on library ""tkinter""
from run_vocabs import Vocabs
from file_translator import Translate
from search_file import *
import json


vocabs = Vocabs()
translate = Translate()
search = Search()

while 1:
    command = input("Please enter your command : ")
    if command.strip() == "-sr":
        translate.start()
    elif command.strip() == "-sv":
        vocabs.vocabs_old_forget()
    elif command.strip() == "-srv":
        search.search()
    elif command == "exit":
        print("exit of program......")
        break

    else:
        print("\n**Error don't have this command **\n")
