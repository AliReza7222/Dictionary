# This file menu.py is for test because this project run on library ""tkinter""
from run_vocabs import Vocabs
from file_translator import Translate
from search_file import *


vocabs = Vocabs()
translate = Translate()
search = Search()


def help_project():
    with open("help.txt", "r") as help_file:
        return help_file.read()


while 1:
    print("**If you need to guide of commands enter help**")
    command = input("Please enter your command : ")
    if command.strip() == "-sr":
        translate.start()
    elif command.strip() == "-sv":
        vocabs.vocabs_old_forget()
    elif command.strip() == "-srv":
        search.search()
    elif command.strip() == "-sds":
        search.show_file_save()
    elif command == "exit":
        print("exit of program......")
        break
    elif command.strip() == "help":
        print(help_project())
    else:
        print("\n**Error don't have this command **\n")
