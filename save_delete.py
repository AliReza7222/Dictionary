import os, re


class Save:

    def directory(self):
        if not (os.path.exists("save_vocab")):
            os.mkdir("save_vocab")

    def save(self, select):
        self.directory()
        if select is not None:
            key = 0
            if not (os.path.exists('save_vocab//save_select.txt')):
                open('save_vocab//save_select.txt', 'w')
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

    def delete(self, select):
        lines = list()
        key = 0
        with open('save_vocab//save_select.txt', 'r') as file_save:
            lines += file_save.readlines()
            for line in lines:
                vocab = re.findall('[^*]\w+[^:]', line.strip('\n'))[0]
                if vocab == select:
                    key = 1
                    break
        if key == 1:
            with open('save_vocab//save_select.txt', 'w') as file_save:
                for line in lines:
                    if re.findall('[^*]\w+[^:]', line.strip('\n'))[0] != select:
                        file_save.write(line)
        else:
            print(f"no exist vocab {select}")

    def show_file_save(self):
        if os.path.exists('save_vocab/save_select.txt'):
            with open('save_vocab/save_select.txt', 'r') as file_save:
                all_lines = file_save.readlines()
                for line in all_lines:
                    enter = input("If you want see next line enter 1 else enter 0 : ")
                    if enter == 0:
                        break
                    else:
                        print(line)
                        delete = input("if you want delete this vocab enter 1 else enter 0 :")
                        if delete == '1':
                            vocab = re.findall("[^*]\w+[^:]", line.strip('\n'))[0]
                            self.delete(vocab)
                            print(f'{vocab} deleted')
        else:
            print("don't have file save")