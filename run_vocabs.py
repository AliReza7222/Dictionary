# b_kh
# run_vocabs
from datetime import datetime
from Config import Config
from file_translator import Translate
import translators


class Vocabs(Config):

    def __init__(self):
        super().__init__()

    @staticmethod
    def translator(text):
        translate = translators.google(text, from_language="en", to_language="fa")
        return translate

    @staticmethod
    def time_enter_exit(key, number=None):
        with open("days that i work english vocabs.txt", "a") as file:
            time = datetime.now()
            if key == "enter":
                line = f"person enter at time : {time.strftime('%A')} {time} \n"
            elif key == 'exit':
                line = f"person exit at time : {time.strftime('%A')} {time} and read up to vocab {number}\n\n"
            file.write(line)

    def vocabs_old_forget(self):
        enter = input("\nvocab\'s old or forget: (forget/old) ? ")
        if enter.strip() == "old":
            line_check = int(input("which line : "))
            self.time_enter_exit("enter")
            print('#--------------- start first vocabs ------------------#')
            list_vocab = Config().old_vocabs()
            list_vocab.sort()
            num = 0
            for v in list_vocab:
                num += 1
                if num >= line_check:
                    try:
                        if int(input("show vocab with key Enter and exit of program with key 0 : ")) == 0:
                            print("exit of program\ngood luck.")
                            self.time_enter_exit("exit", num)
                            break
                    except:
                        print(f"\n\t{num}_{v}\n")
                        if input("do you need to translate this vocab? y\\N : ") == "y":
                            print("This translate be maybe not True ....")
                            print(f"\n\t{self.translator(v)}\n")

        elif enter.strip() == "forget":
            line_check = int(input("which line : "))
            self.time_enter_exit("enter")
            print('#--------------- start first vocabs ------------------#')
            list_vocab = Config().forget_vocab()
            key = list(list_vocab.keys())
            key.sort()
            num = 0
            for k in key:
                num += 1
                if num >= line_check:
                    try:
                        if int(input("show vocab with key Enter and exit of program with key 0 : ")) == 0:
                            print("exit of this part\ngood luck.\n")
                            self.time_enter_exit("exit", num)
                            break
                    except:
                        print(f"\n\t{num}_{k} =\t{list_vocab[k]}\n")
                        if input("do you need to translate this vocab? y\\N : ") == "y":
                            print("This translate be maybe not True ....")
                            print(f"\n\t{self.translator(k)} = {[self.translator(vocab)for vocab in list_vocab[k]]}\n")

        else:
            print("Error enter....")
