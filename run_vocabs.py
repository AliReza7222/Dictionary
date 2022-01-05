# b_kh
# run_vocabs
from datetime import datetime
from main import Config

vocabs = Config()


def time_enter_exit(key):
    with open("days that i work enghlish vocabs.txt", "a") as file:
        time = datetime.now()
        if key == "enter":
            line = f"preson enter at time : {time.strftime('%A')} {time} \n"
        elif key == 'exit':
            line = f"preson exit at time : {time.strftime('%A')} {time} \n\n"
        file.write(line)


enter = input("vocab's old or forget: (forget/old) ? ")
if enter == "old":
    time_enter_exit("enter")
    print('#--------------- start first vocabs ------------------#')
    list_vocab = vocabs.old_vocabs()
    num = 0
    for v in list_vocab:
        num += 1
        try:
            if int(input("show vocab with key Enter and exit of program with key 0 : ")) == 0:
                print("exit of program\ngood luck.")
                break
        except:
            print(f"\n\t{num}_{v}\n")
elif enter == "forget":
    time_enter_exit("enter")
    print('#--------------- start first vocabs ------------------#')
    list_vocab = vocabs.forget_vocab()
    num = 0
    for k, v in zip(list_vocab.keys(), list_vocab.values()):
        num += 1
        try:
            if int(input("show vocab with key Enter and exit of program with key 0 : ")) == 0:
                print("exit of program\ngood luck.")
                time_enter_exit("exit")
                break
        except:
            print(f"\n\t{num}_{k} =\t{v}\n")

else:
    print("Error enter....")
