# b_kh
# run_vocabs
from datetime import datetime
from Config import Config
from file_translator import translator

vocabs = Config()


def time_enter_exit(key):
    with open("days that i work english vocabs.txt", "a") as file:
        time = datetime.now()
        if key == "enter":
            line = f"person enter at time : {time.strftime('%A')} {time} \n"
        elif key == 'exit':
            line = f"person exit at time : {time.strftime('%A')} {time} \n\n"
        file.write(line)


enter = input("\nvocab's old or forget: (forget/old) ? ")
line = int(input("which line : "))
if enter == "old":
    time_enter_exit("enter")
    print('#--------------- start first vocabs ------------------#')
    list_vocab = vocabs.old_vocabs()
    num = 0
    for v in list_vocab:
        num += 1
        if num >= line:
            try:
                if int(input("show vocab with key Enter and exit of program with key 0 : ")) == 0:
                    print("exit of program\ngood luck.")
                    time_enter_exit("exit")
                    break
            except:
                print(f"\n\t{num}_{v}\n")
                if input("do you need to translate this vocab? y\\n : ") == "y":
                    print(f"\n\t{translator(v)}\n")

elif enter == "forget":
    time_enter_exit("enter")
    print('#--------------- start first vocabs ------------------#')
    list_vocab = vocabs.forget_vocab()
    num = 0
    for k, v in zip(list_vocab.keys(), list_vocab.values()):
        num += 1
        if num >= line:
            try:
                if int(input("show vocab with key Enter and exit of program with key 0 : ")) == 0:
                    print("exit of program\ngood luck.")
                    time_enter_exit("exit")
                    break
            except:
                print(f"\n\t{num}_{k} =\t{v}\n")
                if input("do you need to translate this vocab? y\\n : ") == "y":
                    print(f"{translator(k)} = {[translator(vocab)for vocab in v]}")

else:
    print("Error enter....")
