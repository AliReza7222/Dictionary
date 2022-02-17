import tkinter as tk
from PIL import ImageTk, Image
from save_delete import *
from Config import *


class Graphic(Config, Save):

    def window(self, x, y):

        # create a window to name root
        root = tk.Tk()
        root.title("Dictionary")
        # fix size window
        root.geometry(f"{x}x{y}")
        root.minsize(x, y)
        root.maxsize(x, y)
        # add a icon
        root.iconphoto(False, tk.PhotoImage(file="photos/icon_project/dictionary-1876901-1589686.png"))
        return root

    def search_in_forget_list_vocab(self):
        root = self.window(500, 300)
        # add a background
        canvas1 = tk.Canvas(root, width=500, height=300)
        canvas1.pack(fill="both", expand=True)
        bg = ImageTk.PhotoImage(Image.open("photos/background/istockphoto-954677078-170667a.jpg"))
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        font = ("Bahnschrift Light", 10, "bold")
        vocab_search = tk.Text(canvas1, width=30, height=1, bg="#F781F3", fg="#0B2161")
        output = tk.Text(canvas1, width=50, height=5, bg="#F781F3", fg="#0B2161")
        vocab_search.config(font=font)
        output.config(font=font)
        list_answer = ["None"]

        def show():
            vocab = vocab_search.get('1.0', 'end-1c')
            if vocab in self.forget_vocab():
                answer = ''
                answer += f"{vocab}: {self.forget_vocab()[vocab]}"
                print(f"Search vocab [{vocab}]....")
                list_answer.append(answer)
                output.insert(tk.END, answer)
            else:
                output.insert(tk.END, 'not exist this vocab!')

        def clear_text():
            vocab_search.delete('1.0', 'end')
            print("Rest....")
            output.delete('1.0', 'end')

        w_label = tk.Label(canvas1, text="YOUR WELCOME\nThis Department is for search in list-forget-vocab",
                           bg="#81DAF5")
        line_label = tk.Label(canvas1, text="-"*100, fg="#A901DB", bg="#81DAF5")
        search_label = tk.Label(canvas1, text="Enter-vocab:", bg="#81DAF5")
        output_label = tk.Label(canvas1, text="Out-Put:", bg="#81DAF5")
        button = tk.Button(canvas1, command=show, text="Search", bg="#8A0886", fg="#2E9AFE",
                           activebackground="#81DAF5", activeforeground="#8A0886")
        button_clear = tk.Button(canvas1, text="Rest", command=clear_text, bg="#8A0886", fg="#2E9AFE",
                                 activebackground="#81DAF5", activeforeground="#8A0886")
        button_save_vocab = tk.Button(canvas1, text="Save", command=lambda: self.save(list_answer[-1]+"\n"),
                            bg="#8A0886", fg="#2E9AFE", activebackground="#81DAF5", activeforeground="#8A0886")

        w_label.pack()
        line_label.pack()
        search_label.pack()
        vocab_search.pack()
        output_label.pack()
        output.pack()
        button.pack()
        button_save_vocab.pack()
        button_clear.pack()

        root.mainloop()

    def vocabs_old_forget(self):
        root =self.window(500, 500)
        root.mainloop()

