import tkinter as tk
from PIL import ImageTk, Image
from search_file import *


class Graphic(Search):

    # create a window to name root
    root = tk.Tk()
    root.title("Dictionary")
    # fix size window
    root.geometry("500x300")
    root.minsize(500, 300)
    root.maxsize(500, 300)
    # add a icon
    root.iconphoto(False, tk.PhotoImage(file="photos/icon_project/dictionary-1876901-1589686.png"))
    # add a background
    canvas1 = tk.Canvas(root, width=500, height=300)
    canvas1.pack(fill="both", expand=True)
    bg = ImageTk.PhotoImage(Image.open("photos/background/istockphoto-954677078-170667a.jpg"))
    canvas1.create_image(0, 0, image=bg, anchor="nw")

    def search_in_forget_list_vocab(self):
        vocab_search = tk.Text(self.canvas1, width=30, height=1)
        output = tk.Text(self.canvas1, width=50, height=5)

        def show():
            vocab = vocab_search.get('1.0', 'end-1c')
            answer = ''
            if vocab in self.forget_vocab():
                answer += f"{vocab}: {self.forget_vocab()[vocab]}"
                output.insert(tk.END, answer)
            else:
                output.insert(tk.END, 'not exist this vocab!')

        def clear_text():
            vocab_search.delete('1.0', 'end')
            output.delete('1.0', 'end')

        w_label = tk.Label(self.canvas1, text="YOUR WELCOME\nThis Department is for search in list-forget-vocab",
                           bg="#5C9EAF")
        line_label = tk.Label(self.canvas1, text="-"*100, fg="#2A2DEC", bg="#BF4EF3")
        search_label = tk.Label(self.canvas1, text="Enter-vocab:")
        output_label = tk.Label(self.canvas1, text="Out-Put:")
        button = tk.Button(self.canvas1, command=show, text="Search")
        button_clear = tk.Button(self.canvas1, text="rest", command=clear_text)

        w_label.pack()
        line_label.pack()
        search_label.pack()
        vocab_search.pack()
        output_label.pack()
        output.pack()
        button.pack()
        button_clear.pack()

        self.root.mainloop()


g = Graphic()
g.search_in_forget_list_vocab()
