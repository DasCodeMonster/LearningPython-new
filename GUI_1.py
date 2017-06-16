from tkinter import *
class App:
    def __init__(self, master, title, geometry, Ausgabe):
		self.title = title
		self.geometry = geometry
		self.Ausgabe = Ausgabe
        Label(master, text=self.Ausgabe, fg="light green", font="Times").pack()
        self.button = Button(master, text="Quit", fg="red", bg = "light blue",command = master.quit)
        self.button.pack(side=BOTTOM)
        self.button.place(x=50, y=150)
        self.hi_there = Button(master, text="Hello", command = self.say_hi)
        self.hi_there.pack(side=BOTTOM)
        self.hi_there.place(x=90, y=150)

    def say_hi(self):
        print("Hallo!")

root = Tk()
root.title("First GUI")
root.geometry("170x200+30+30")
window = Tk()
window.title("2. Fenster")
app2 = App(window, "2. Fenster", "400x400+30+30")
app = App(root, "First GUI", "170x200+30+30", "Hier steht Text!")
root.mainloop()
window.mainloop()
# root.destroy()