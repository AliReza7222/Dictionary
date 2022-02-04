"""
    this file is search vocab offline this project
"""
from Config import Config
from save_delete import *


class Search(Config, Save):
    def __init__(self):
        super().__init__()

    def search(self):
        print("you can search vocab in (list_forget_vocabs)......")
        vocab = input("please enter your vocab: ").strip()
        if vocab in self.forget_vocab():
            text = f"{vocab}: {self.forget_vocab()[vocab]}\n"
            print(text)
            command = input("if you want save this vocab enter 1 else enter 0: ")
            if command == '1':
                self.save(text)
            else:
                print("ok")
        else:
            print("this vocab not exist")
