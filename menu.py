# This file menu.py is for test because this project run on library ""tkinter""
from run_vocabs import Vocabs
from file_translator import Translate


vocabs = Vocabs()
translate = Translate()

while 1:
    command = input("Please enter your command : ")
    if command.strip() == "-sr":
        translate.start()
    elif command.strip() == "-sv":
        vocabs.vocabs_old_forget()
    elif command == "exit":
        print("exit of program......")
        break
