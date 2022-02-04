import translators
from save_delete import *


class Translate(Save):

    def start(self):
        text = input("Please enter your text : ")
        list_language = ["english_to_farsi", "farsi_to_english", "farsi_to_chinese", "english_to_chinese",
                         "english_to_arab", "farsi_to_arab", "farsi_to_german", "english_to_german",
                         "english_to_spain", "farsi_to_spain"]

        print("languages : ")
        for num, language in enumerate(list_language, 0):
            print(f"\t{num}_{language}")
        select = int(input("please enter your select number_language : "))
        mean = None
        if select == 0:
            mean = translators.google(text, from_language="en", to_language="fa")
            print(mean)

        elif select == 1:
            mean = translators.google(text, from_language="fa", to_language="en")
            print(mean)

        elif select == 2:
            mean = translators.google(text, from_language="fa", to_language="hi")
            print(mean)

        elif select == 3:
            mean = translators.google(text, from_language="en", to_language="hi")
            print(mean)

        elif select == 4:
            mean = translators.google(text, from_language="en", to_language="ar")
            print(mean)

        elif select == 5:
            mean = translators.google(text, from_language="fa", to_language="ar")
            print(mean)

        elif select == 6:
            mean = translators.google(text, from_language="fa", to_language="de")
            print(mean)

        elif select == 7:
            mean = translators.google(text, from_language="en", to_language="de")
            print(mean)

        elif select == 8:
            mean = translators.google(text, from_language="en", to_language="es")
            print(mean)

        elif select == 9:
            mean = translators.google(text, from_language="fa", to_language="es")
            print(mean)
        text = f"{text} : mean is {mean}\n"
        if input("you want save this text y/N: ") == 'y':
            self.save(text)
        print("this translate maybe not True .")
