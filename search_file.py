"""
    this file is search vocab offline this project
"""
from Config import Config
import os


class Search(Config):
    def __init__(self):
        super().__init__()

    def directory(self):
        if not (os.path.exists("save_vocab")):
            os.mkdir("save_vocab")

    def save(self, select):
        self.directory()
        if select is not None:
            key = 0
            with open("save_vocab//save_select.txt", "r") as text:
                while True:
                    line = text.readline()
                    if line == select:
                        print("this vocab exist !")
                        break
                    elif line == "":
                        key = 1
                        break
            if key == 1:
                with open("save_vocab//save_select.txt", "a") as text:
                    text.write(select)
                    print("saved.")

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


test = Search()
test.search()
