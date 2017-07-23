import tkinter as tk
# from tkinter import scrolledtext
# from tkinter import constants
from tkinter import dnd
# from tkinter import filedialog


class Fenster:
    def __init__(self, size, title, master=None, inhalt=None):
        self.size = size  # tuple int
        self.title = title  # string name
        self.inhalt = inhalt
        self.master = master
        if self.master is None:
            self.run()
        else:
            self.child()
        # self.dragAndDrop()

    def run(self):
        root = tk.Tk()  # create window
        root.geometry(str(self.size[0]) + "x" + str(self.size[1]))  # set the size
        root.title(self.title)  # set the tile
        self.dndButton = tk.Button(root, text="Acivate Drag and Drop")
        self.dndButton.bind("<ButtonPress>", self.startdragAndDrop)
        self.dndButton.pack(side="top")
        self.inhaltLabel = tk.Label(root, text=self.inhalt)
        self.inhaltLabel.pack(side="bottom")
        self.child()
        root.mainloop()

    def child(self):
        child = tk.Toplevel(self.master)
        childLabel = tk.Label(child, text=self.inhalt)
        childLabel.pack(side="bottom")

    def startdragAndDrop(self, event):
        self.dndButton.configure(command=self.endDragAndDrop)
        dnd.dnd_start(self.dndButton, event)

    def endDragAndDrop(self):
        pass


if __name__ == "__main__":
    Fenster((100, 100), "Hallo", inhalt="Mir geht es gut :)")