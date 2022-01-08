import translators


class Translate:
    text = input("Please enter your text : ")

    def start(self):
        list_language = ["english_to_farsi", "farsi_to_english", "farsi_to_chinese", "english_to_chinese",
                         "english_to_arab", "farsi_to_arab", "farsi_to_german", "english_to_german",
                         "english_to_spain", "farsi_to_spain"]

        print("languages : ")
        for num, language in enumerate(list_language, 0):
            print(f"\t{num}_{language}")
        select = int(input("please enter your select number_language : "))
        if select == 0:
            print(translators.google(self.text, from_language="en", to_language="fa"))

        elif select == 1 :
            print(translators.google(self.text, from_language="fa", to_language="en"))

        elif select == 2:
            print(translators.google(self.text, from_language="fa", to_language="hi"))

        elif select == 3:
            print(translators.google(self.text, from_language="en", to_language="hi"))

        elif select == 4:
            print(translators.google(self.text, from_language="en", to_language="ar"))

        elif select == 5:
            print(translators.google(self.text, from_language="fa", to_language="ar"))

        elif select == 6:
            print(translators.google(self.text, from_language="fa", to_language="de"))

        elif select == 7:
            print(translators.google(self.text, from_language="en", to_language="de"))

        elif select == 8:
            print(translators.google(self.text, from_language="en", to_language="es"))

        elif select == 9:
            print(translators.google(self.text, from_language="fa", to_language="es"))
        print("this translate maybe not True .")

