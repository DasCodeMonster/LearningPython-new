# Erstellen einer GUI
from tkinter import *
import tkinter.filedialog as tkf

class Fenster:
	def __init__(self, klasse):
		root.title("Fenster: Root")
		# root.geometry("170x200+30+30")
		Schrift = Label(root, text="Root: Fenster 1", fg="white", bg="dark blue")
		Schrift.pack()
		self.button = Button(root, text="Quit", fg="red", command=root.quit)
		self.button2 = Button(root, text="Browse Directory", command=tkf.askdirectory())
		self.button.pack()
		self.button2.pack()
		root.mainloop()

class Fenster2:
	def __init__(self, klasse):
		window.title("Fenster: Window")
		# window.geometry("170x200+30+30")
		Schrift = Label(window, text="Window: Fenster 1", fg="white", bg="dark blue")
		Schrift.pack()
		self.button = Button(window, text="Quit", fg="red", command=window.quit)
		self.button.pack()
		window.mainloop()

root = Tk()
RootFenster = Fenster(root)
# window = Tk()
# WindowFenster = Fenster2(window)
# root = Tk()
# frame = Frame(root)
# frame.pack()
# root.mainloop()
