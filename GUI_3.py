import tkinter as tk
import tkinter.filedialog as tkf

Directory = None
Filename = "Peter"

def DeinText(event):
    print(e.get())

def Browse():
    global Directory
    Directory = tkf.askdirectory()
    d.set(Directory)
    print(Directory)

def SaveFile():
    print(str(Directory) + "\\" + Filename + ".txt")
    f = open(Directory + "\\" + Filename + ".txt", "w")
    f.write(e.get())

if __name__ == "__main__":
    root = tk.Tk()
    menu = tk.Menu(root)
    root.config(menu=menu)
    Filemenu = tk.Menu(menu)
    menu.add_cascade(label="File", menu=Filemenu)
    menu.add_cascade(label="Help", menu=Filemenu)
    root.title("GUI")
    d = tk.StringVar()
    tk.Label(root, text="Browse your directory:").grid(row=0)
    tk.Button(root, text="Browse", command=Browse).grid(row=0, column=2)
    tk.Label(root, textvariable=d).grid(row=0, column=1)
    tk.Label(root, text="Dein Text: ").grid(row=2, sticky="e")
    b = tk.Button(root, text="Print", command=DeinText)
    b.bind("<Return>", DeinText)
    b.grid(row=2, column=2, pady=4)
    tk.Button(root, text="Quit", command=root.quit).grid(row=3)
    tk.Button(root, text="Save File", command=SaveFile).grid(row=3, column=1)
    e = tk.Entry(root)
    e.bind("<Return>", DeinText)
    e.insert(10, "Text")
    e.grid(row=2, column=1,sticky="w")
    root.update_idletasks()
    root.mainloop()