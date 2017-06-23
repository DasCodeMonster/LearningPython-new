# Vokabeltrainer mit GUI
import tkinter as tk
import tkinter.filedialog as tkf
from functools import partial
import time
import random
import io
import os

directory = None
chosen = None
b2 = None
b3 = None
correct_answer = None
vardirectory = None
l1 = None
e1 = None
e2 = None
vocs = None
english = None
rd = []
re = []
rda = []
rea = []
path = ""
lineinfile = 0

def help():
    print("help")


# def ask_window():
#     ask = tk.Tk()
#     ask.title("VokTrainer")
#     ask.configure(background="white")
#     ask.resizable(0,0)
#     b1 = tk.Button(ask, text="Choose directory", command=partial(askdir, ask), background="white")
#     b1.bind("<Return>", partial(askdir, ask))
#     b1.pack(pady=5)
#     ask.mainloop()


# def askdir(ask, event=None):
#     global directory
#     global chosen
#     directory = tkf.askdirectory(initialdir="C:\\Voktrainer")
#     if directory == "":
#         chosen = False
#     else:
#         print(directory)
#         chosen = True
#     print(chosen)
#     ask.destroy()
#     init_liste()


def init_liste():
    try:
        f = open(directory + "\\vocs.txt", "r")
    except FileNotFoundError:
        f = open(directory + "\\vocs.txt", "w+")
    global rd
    global rda
    global re
    global rea
    rda = []
    rd = []
    re = []
    rea = []
    for line in f:
        rd.append(line.rstrip().split(';')[1])
        re.append(line.rstrip().split(';')[2])
    f.close()


def app():
    root = tk.Tk()
    root.title("Vokabeltrainer")
    root.resizable(0,0)
    root.configure(background="white")
    global german
    global english
    german = tk.StringVar()
    english = tk.StringVar()
    menu = tk.Menu(root)
    root.config(menu=menu)
    helpmenu = tk.Menu(menu)
    windowmenu = tk.Menu(menu)
    bearbeiten = tk.Menu(menu)
    bearbeiten.add_command(label="Einträge bearbeiten", command=partial(delete_entrys_window, root))
    helpmenu.add_command(label="Help", command=help)
    windowmenu.add_command(label="Test 2", command=help)
    menu.add_cascade(label="Help", menu=helpmenu)
    menu.add_cascade(label="Test", menu=windowmenu)
    menu.add_cascade(label="Bearbeiten", menu=bearbeiten)
    global directory
    global l1
    l1 = tk.Label(root, text="Directory: " + directory, background="white")
    l1.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=3)
    b0 = tk.Button(root, text="Browse", command=partial(change_directory, root), background="white")
    b0.bind("<Return>", partial(change_directory, root))
    b0.grid(row=0, column=2, sticky="w", padx=5, pady=3)
    tk.Label(root, text="Vokabeln einspeichern:", background="white").grid(row=1, column=0, sticky="w", padx=5, pady=3)
    tk.Label(root, text="Deutsch:", background="white").grid(row=2, column=0, sticky="e", padx=5, pady=3)
    global e1
    global e2
    e1 = tk.Entry(root, background="lightgrey")
    e2 = tk.Entry(root, background="lightgrey")
    e1.bind("<Return>", partial(next_box, e2))
    e1.grid(row=2, column=1, sticky="w", padx=5, pady=3)
    e1.focus_force()
    tk.Label(root, text="English:", background="white").grid(row=3, column=0, sticky="e", padx=5, pady=3)
    e2.bind("<Return>", partial(savevoc, root))
    e2.grid(row=3, column=1, sticky="w", padx=5, pady=3)
    b1 = tk.Button(root, text="Save Voc.", command=partial(savevoc, root), background="white")
    b1.bind("<Return>", partial(savevoc, root))
    b1.grid(row=4, column=1, sticky="e", padx=5, pady=3)
    global b2
    b2 = tk.Button(root, text="Show all", command=partial(show_all, root), background="white")
    b2.bind("<Return>", partial(show_all, root))
    b2.grid(row=4, column=1, sticky="w", padx=5, pady=3)
    global b3
    b3 = tk.Button(root, text="Abfrage", command=partial(random_abfrage, root), background="white")
    b3.bind("<Return>", partial(random_abfrage, root))
    b3.grid(row=4, column=0, sticky="e", padx=5, pady=3)
    b4 = tk.Button(root, text="Quit", command=partial(quit_window, root), background="white")
    b4.bind("<Return>", partial(quit_window, root))
    b4.grid(row=4, column=0, sticky="w", padx=5, pady=3)
    b5 = tk.Button(root, text="Delete Entrys", command=partial(delete_entrys_window, root), background="white")
    b5.bind("<Return>", partial(delete_entrys_window, root))
    # b5.grid(row=4, column=2, sticky="w", padx=5, pady=3)
    root.mainloop()


def next_box(e2, event=None):
    e2.focus()


def change_directory(root, event=None):
    global l1
    l1.destroy()
    global directory
    tempdirectory = tkf.askdirectory()
    if tempdirectory != "":
        directory = tempdirectory
        open("CONFIG.config", "w").write("PATH=" + directory)
    print(directory)
    print(tempdirectory)
    l1 = tk.Label(root, text="Directory: " + directory, background="white")
    l1.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=3)
    init_liste()


def savevoc(root, event=None):
    vocs = io.StringIO()
    try:
        with open(directory + "\\vocs.txt", "r") as f:
            vocs.write(f.read() + '\n')
    except FileNotFoundError:
        pass
    global e1
    global e2
    if e1.get() == "":
        print("Darf nicht leer sein!")
        e1.insert(0, "Darf nicht leer sein!")
    if e2.get() == "":
        e2.insert(0, "Darf nicht leer sein!")
        print("Darf nicht leer sein")
    if e1.get() == "Darf nicht leer sein!" or e2.get() == "Darf nicht leer sein!":
        pass
    else:
        global lineinfile
        print(str(lineinfile + 1) + ";" + e1.get() + ';' + e2.get(), file=vocs)
        lineinfile += 1
        with open("CONFIG.config", "w") as file:
            file.write("PATH=" + directory)
            file.write("\nX=" + str(lineinfile))
        print(repr(vocs.getvalue().strip()))
        with open(directory + "\\vocs.txt", "w") as f:
            f.write(vocs.getvalue().strip())
        print("Saved german Voc")
        print("Saved english Voc")
        e1.delete(0, "end")
        e2.delete(0, "end")
    init_liste()
    e1.focus()
    update()
    root.update()


def random_abfrage(root, event=None):
    init_liste()
    abfragel1 = tk.Label(root, text="Abfrage", background="white")
    abfragel1.grid(row=7, column=0, sticky="w", padx=5, pady=3)
    abfragel2 = tk.Label(root, text="Deutsch:", background="white")
    abfragel2.grid(row=8, column=0, sticky="w", padx=5, pady=3)
    abfragel3 = tk.Label(root, text="English:", background="white")
    abfragel3.grid(row=8, column=1, sticky="w", padx=5, pady=3)
    root.update()
    x = random.randint(1, 2)
    print(x)
    global rd
    vocs = tk.StringVar()
    xd = random.randint(0, len(rd) - 1)
    vocs.set(rd[xd])
    global re
    english = tk.StringVar()
    xe = random.randint(0, len(re) - 1)
    english.set(re[xe])
    abfragel4 = tk.Label(root, textvariable=vocs, background="white")
    abfragel5 = tk.Label(root, textvariable=english, background="white")
    global correct_answer
    correct_answer = tk.StringVar()
    abfragel6 = tk.Label(root, textvariable=correct_answer, background="white")
    evoc = tk.Entry(root, bg="lightgrey")
    evoc.bind("<Return>",
              partial(compare_evoc, evoc, xd, root, abfragel1, abfragel2, abfragel3, abfragel4, abfragel5,
                      abfragel6))
    dvoc = tk.Entry(root, bg="lightgrey")
    dvoc.bind("<Return>",
              partial(compare_dvoc, dvoc, xe, root, abfragel1, abfragel2, abfragel3, abfragel4, abfragel5,
                      abfragel6))
    global b3
    b3.destroy()
    b3 = tk.Button(root, text="Hide: Abfrage", relief="raised",
                   command=partial(hide_abfrage, abfragel1, abfragel2, abfragel3, abfragel4, abfragel5, evoc, dvoc,
                                   root), background="white")
    b3.bind("<Return>", partial(hide_abfrage, abfragel1, abfragel2, abfragel3, abfragel4, abfragel5, evoc, dvoc, root))
    b3.grid(row=4, column=0, sticky="e", padx=5, pady=3)
    if x == 1:
        abfragel4.grid(row=9, column=0, sticky="w", padx=5, pady=3)
        evoc.grid(row=9, column=1, sticky="w", padx=5, pady=3)
        evoc.focus()
    elif x == 2:
        abfragel5.grid(row=9, column=1, sticky="w", padx=5, pady=3)
        dvoc.grid(row=9, column=0, sticky="w", padx=5, pady=3)
        dvoc.focus()


def compare_evoc(evoc, xd, root, label1, label2, label3, label4, label5, label6,  event=None):
    global correct_answer
    global re
    # global rea
    # if evoc.get() == rea[xd]
    if evoc.get() == re[xd]:
        print("Correct!")
        correct_answer.set("Correct!")
        # print(re)
        # del re[xd]
        # print(re)
        # if re is []:
        #     init_liste()
    else:
        print("Wrong! The right answer was ", re[xd])
        correct_answer.set("Wrong! The right answer was " + re[xd])
    label6.grid(row=10, column=0, columnspan=2, sticky="w", padx=5, pady=3)
    root.update()
    time.sleep(1.5)
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    label6.destroy()
    evoc.destroy()
    random_abfrage(root)


def compare_dvoc(dvoc, xe, root, label1, label2, label3, label4, label5, label6, event=None):
    global correct_answer
    global rd
    # global rda
    # if dvoc.get() == rda[xe]
    if dvoc.get() == rd[xe]:
        print("Correct!")
        correct_answer.set("Correct!")
        # print(rd)
        # del rd[xe]
        # print(rd)
        # if rd is []:
        #     init_liste()
    else:
        print("Wrong! The right answer was ", rd[xe])
        correct_answer.set("Wrong the right answer was: " + rd[xe])
    label6.grid(row=10, column=0, columnspan=2, sticky="w", padx=5, pady=3)
    root.update()
    time.sleep(1.5)
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    label6.destroy()
    dvoc.destroy()
    random_abfrage(root)


def hide_abfrage(label1, label2, label3, label4, label5, entry1, entry2, root, event=None):
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    entry1.destroy()
    entry2.destroy()
    global b3
    b3.destroy()
    b3 = tk.Button(root, text="Abfrage", command=partial(random_abfrage, root), background="white")
    b3.bind("<Return>", partial(random_abfrage, root))
    b3.grid(row=4, column=0, sticky="e", padx=5, pady=3)

def update():
    showvocs = open(directory + "\\vocs.txt")
    deutsch, englisch = [], []
    for line in showvocs:
        deutsch.append(line.rstrip().split(';')[1])
        englisch.append(line.rstrip().split(';')[2])
    
#     showenglish = open(directory + "\\English.txt")
    german.set("\n".join(deutsch))
    english.set("\n".join(englisch))
    
def show_all(root, event=None):
    global german
    global english
    update()
    showl1 = tk.Label(root, text="Deutsch:", background="white")
    showl1.grid(row=5, column=0, sticky="w", padx=5, pady=3)
    showl2 = tk.Label(root, textvariable=german, background="white")
    showl2.grid(row=6, column=0, sticky="w", padx=5, pady=3)
    showl3 = tk.Label(root, text="English", background="white")
    showl3.grid(row=5, column=1, sticky="w", padx=5, pady=3)
    showl4 = tk.Label(root, textvariable=english, background="white")
    showl4.grid(row=6, column=1, sticky="w", padx=5, pady=3)
    global b2
    b2.destroy()
    b2 = tk.Button(root, text="Hide", command=partial(show_nothing, showl1, showl2, showl3, showl4, root),
                   background="white")
    b2.bind("<Return>", partial(show_nothing, showl1, showl2, showl3, showl4, root))
    b2.grid(row=4, column=1, sticky="w", padx=5, pady=3)


def show_nothing(label1, label2, label3, label4, root, event=None):
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    global b2
    b2 = tk.Button(root, text="Show all", command=partial(show_all, root), background="white")
    b2.bind("<Return>", partial(show_all, root))
    b2.grid(row=4, column=1, sticky="w", padx=5, pady=3)


def delete_entrys_window(root, event=None):
    delete = tk.Toplevel()
    delete.title("Delete Vocs")
    delete.resizable(0,0)
    delete.configure(background="white")
    delete.focus_force()
    tk.Label(delete, text="Deutsch:", background="white").grid(row=0, column=0, sticky="w", padx=5, pady=3)
    tk.Label(delete, text="English:", background="white").grid(row=0, column=1, sticky="e", padx=5, pady=3)
    vocs = open(directory + "\\vocs.txt")
    x=1
    for line in vocs:
        tk.Label(delete, text=line.rstrip().split(";")[1], background="white").grid(row=x, column=0)
        tk.Label(delete, text=line.rstrip().split(";")[2], background="white").grid(row=x, column=1)
        deletebutton = tk.Button(delete, text="Delete", command=partial(delete_entrys, x, root, delete), background="red")
        deletebutton.bind("<Return>", partial(delete_entrys, x, root, delete))
        deletebutton.grid(row=x, column=2, sticky="w", padx=5, pady=3)
        x += 1
    root.update()
    delete.update()
    delete.mainloop()
    root.focus_force()
    e1.focus()


def delete_entrys(x, root, delete_window, event=None):
    file = open(directory + "\\vocs.txt")
    text = ""
    y = 1
    for line in file:
        if y == x:
            break
        text += str(line) #  .rstrip()) #  .split())
        y += 1
    anotherfile = open(directory + "\\test.txt", "w")
    text2 = ""
    for line in file:
        if y >= x:
            text2 += str(line)
        y += 1
    anotherfile.write(text + text2)
    print(text)
    anotherfile.close()
    anotherfile = open(directory + "\\test.txt", "r")
    fileline = 0
    thefile = open(directory + "\\test2.txt", "w")
    for line in anotherfile:
        if line.split(";")[0] is not fileline:
            thefile.write(str(fileline) + ";" + str(line.split(";")[1]) + ";" + str(line.split(";")[2]))
            print(str(fileline) + ";" + str(line.split(";")[1]) + str(line.split(";")[2]))
        fileline += 1
    thefile.close()
    anotherfile.close()
    thefile = open(directory + "\\test2.txt", "r")
    newvocsfile = open(directory + "\\vocs.txt", "w")
    newvocsfile.write(thefile.read())
    newvocsfile.close()
    thefile.close()
    os.remove(directory + "\\test.txt")
    os.remove(directory + "\\test2.txt")
    newvocsfile = open(directory + "\\vocs.txt")
    newlines = ""
    for line in newvocsfile:
        newlines = line.split(";")[0]
    newvocsfile.close()
    config = open("CONFIG.config", "w")
    config.write("PATH=" + directory + "\n" + "X=" + str(newlines).strip("['").rstrip("']"))
    config.close()
    root.update()
    delete_window.update()



def quit_window(root, event=None):
    root.quit()


def path_is(event=None):
    global path
    global directory
    path = tkf.askdirectory()
    if path is not "":
        config = open("CONFIG.config", "w")
        config.write("PATH=" + path)
        config.write("\nX=0")
        config.close()
        config = open("CONFIG.config", "r")
        x = 0
        for line in config:
            if x == 0:
                directory = line.rstrip().split("=")[1]
            if x == 1:
                lineinfile = line.rstrip().split("=")[1]
            x += 1
        install.destroy()


if __name__ == "__main__":
    try:
        path = open("CONFIG.config", "r")
        x = 0
        for line in path:
            if x == 0:
                directory = line.rstrip().split("=")[1]
            if x == 1:
                lineinfile = int(line.rstrip().split("=")[1])
            x += 1
        print(lineinfile)
        # directory = path.read().rstrip().split("=")[1]
        # lineinfile = path.read().rstrip().split("=")[0]
    except FileNotFoundError:
        install = tk.Tk()
        install.title("VokTrainer")
        install.configure(background="white")
        install.resizable(0,0)
        tk.Label(text="Choose a Path", bg="white").grid()
        b = tk.Button(text="OK", command=path_is, background="white")
        b.bind("<Return>", path_is)
        b.grid()
        install.mainloop()
        if path == "":
            quit()
    print(directory)
    app()
