import tkinter as tk
from tkinter import scrolledtext
from tkinter import constants
# from tkinter import filedialog


class Fenster:
    def __init__(self, size, title):
        self.size = size  # tuple int
        print(self.size)
        self.title = title  # string name
        self.run()
        self.inhalt = None

    def run(self):
        root = tk.Tk()  # create window
        print(root.size())  # set the size
        scrolledText = scrolledtext.ScrolledText(root)
        scrolledText.insert(constants.CURRENT, "Hallo")
        scrolledText.grid()
        root.title(self.title)  # set the tile
        root.mainloop()

if __name__ == "__main__":
    Fenster(20, "Hallo")