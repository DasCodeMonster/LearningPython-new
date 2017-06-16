# Vokabeltrainer mit GUI
import tkinter as tk
import tkinter.filedialog as tkf
from functools import partial
import time
import random
import io

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

def help():
    print("help")

def ask_window():
    ask = tk.Tk()
    ask.title("VokTrainer")
    b1 = tk.Button(ask, text="Choose directory", command=partial(askdir, ask))
    b1.bind("<Return>", partial(askdir, ask))
    b1.pack(pady=5)
    ask.mainloop()


def askdir(ask, event=None):
    global directory
    global chosen
    directory = tkf.askdirectory(initialdir="C:\\Voktrainer")
    if directory == "":
        chosen = False
    else:
        print(directory)
        chosen = True
    print(chosen)
    ask.destroy()
    init_liste()


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
        rd.append(line.rstrip().split(';')[0])
        re.append(line.rstrip().split(';')[1])
    f.close()


def app():
    root = tk.Tk()
    root.title("Vokabeltrainer")
    global german
    global english
    german = tk.StringVar()
    english = tk.StringVar()
    menu = tk.Menu(root)
    root.config(menu=menu)
    helpmenu = tk.Menu(menu)
    windowmenu = tk.Menu(menu)
    helpmenu.add_command(label="Help", command=help)
    windowmenu.add_command(label="Test 2", command=help)
    menu.add_cascade(label="Help", menu=helpmenu)
    menu.add_cascade(label="Test", menu=windowmenu)
    global directory
    global l1
    l1 = tk.Label(root, text="Directory: " + directory)
    l1.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=3)
    b0 = tk.Button(root, text="Browse", command=partial(change_directory, root))
    b0.bind("<Return>", partial(change_directory, root))
    b0.grid(row=0, column=2, sticky="w", padx=5, pady=3)
    tk.Label(root, text="Vokabeln einspeichern:").grid(row=1, column=0, sticky="w", padx=5, pady=3)
    tk.Label(root, text="Deutsch:").grid(row=2, column=0, sticky="e", padx=5, pady=3)
    global e1
    global e2
    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e1.bind("<Return>", partial(next_box, e2))
    e1.grid(row=2, column=1, sticky="w", padx=5, pady=3)
    e1.focus_force()
    tk.Label(root, text="English:").grid(row=3, column=0, sticky="e", padx=5, pady=3)
    e2.bind("<Return>", partial(savevoc, root))
    e2.grid(row=3, column=1, sticky="w", padx=5, pady=3)
    b1 = tk.Button(root, text="Save Voc.", command=partial(savevoc, root))
    b1.bind("<Return>", partial(savevoc, root))
    b1.grid(row=4, column=1, sticky="e", padx=5, pady=3)
    global b2
    b2 = tk.Button(root, text="Show all", command=partial(show_all, root))
    b2.bind("<Return>", partial(show_all, root))
    b2.grid(row=4, column=1, sticky="w", padx=5, pady=3)
    global b3
    b3 = tk.Button(root, text="Abfrage", command=partial(random_abfrage, root))
    b3.bind("<Return>", partial(random_abfrage, root))
    b3.grid(row=4, column=0, sticky="e", padx=5, pady=3)
    b4 = tk.Button(root, text="Quit", command=partial(quit_window, root))
    b4.bind("<Return>", partial(quit_window, root))
    b4.grid(row=4, column=0, sticky="w", padx=5, pady=3)
    b5 = tk.Button(root, text="Delete Entrys", command=partial(delete_entrys_window, root))
    b5.bind("<Return>", partial(delete_entrys_window, root))
    b5.grid(row=4, column=2, sticky="w", padx=5, pady=3)
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
    print(directory)
    print(tempdirectory)
    l1 = tk.Label(root, text="Directory: " + directory)
    l1.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=3)
    init_liste()

    # root.update()


def savevoc(root, event=None):
    vocs = io.StringIO()
    try:
        with open(directory + "\\vocs.txt", "r") as f:
            vocs.write(f.read() + '\n')
    except FileNotFoundError:
        pass
#     while True:
#         try:
#             efile = open(directory + "\\Deutsch.txt", "a")
#             break
#         except Exception:
#             open(directory + "\\Deutsch.txt", "w")
#             continue
#     while True:
#         try:
#             dfile = open(directory + "\\English.txt", "a")
#             break
#         except Exception:
#             open(directory + "\\English.txt", "w")
#             continue
    global e1
    global e2
    if e1.get() == "":
        print("Darf nicht leer sein!")
        # e1.destroy()
        # e1 = tk.Entry(root)
        e1.insert(0, "Darf nicht leer sein!")
#         e1.grid(row=2, column=1, sticky="w", padx=5, pady=3)
    if e2.get() == "":
        # e2.destroy()
        # e2 = tk.Entry(root)
        e2.insert(0, "Darf nicht leer sein!")
#         e2.grid(row=3, column=1, sticky="w", padx=5, pady=3)
        print("Darf nicht leer sein")
    if e1.get() == "Darf nicht leer sein!" or e2.get() == "Darf nicht leer sein!":
        pass
    else:
        print(e1.get() + ';' + e2.get(), file=vocs)
        print(repr(vocs.getvalue().strip()))
        with open(directory + "\\vocs.txt", "w") as f:
            f.write(vocs.getvalue().strip())
#         with open("Test.txt", 'w') as f:
#             f.write(vocs.getvalue().rstrip())
#         efile.write(e1.get() + "\n")
        print("Saved german Voc")
#         dfile.write(e2.get() + "\n")
        print("Saved english Voc")
        e1.delete(0, "end")
        e2.delete(0, "end")
#     efile.close()
#     dfile.close()
    init_liste()
    e1.focus()
    update()
    root.update()


def random_abfrage(root, event=None):
    abfragel1 = tk.Label(root, text="Abfrage")
    abfragel1.grid(row=7, column=0, sticky="w", padx=5, pady=3)
    abfragel2 = tk.Label(root, text="Deutsch:")
    abfragel2.grid(row=8, column=0, sticky="w", padx=5, pady=3)
    abfragel3 = tk.Label(root, text="English:")
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
    abfragel4 = tk.Label(root, textvariable=vocs)
    abfragel5 = tk.Label(root, textvariable=english)
    global correct_answer
    correct_answer = tk.StringVar()
    abfragel6 = tk.Label(root, textvariable=correct_answer)
    evoc = tk.Entry(root)
    evoc.bind("<Return>",
              partial(compare_evoc, evoc, xd, root, abfragel1, abfragel2, abfragel3, abfragel4, abfragel5,
                      abfragel6))
    dvoc = tk.Entry(root)
    dvoc.bind("<Return>",
              partial(compare_dvoc, dvoc, xe, root, abfragel1, abfragel2, abfragel3, abfragel4, abfragel5,
                      abfragel6))
    global b3
    b3.destroy()
    b3 = tk.Button(root, text="Hide: Abfrage", relief="raised",
                   command=partial(hide_abfrage, abfragel1, abfragel2, abfragel3, abfragel4, abfragel5, evoc, dvoc,
                                   root))
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
    b3 = tk.Button(root, text="Abfrage", command=partial(random_abfrage, root))
    b3.bind("<Return>", partial(random_abfrage, root))
    b3.grid(row=4, column=0, sticky="e", padx=5, pady=3)

def update():
    showvocs = open(directory + "\\vocs.txt")
    deutsch, englisch = [], []
    for line in showvocs:
        deutsch.append(line.rstrip().split(';')[0])
        englisch.append(line.rstrip().split(';')[1])
    
#     showenglish = open(directory + "\\English.txt")
    german.set("\n".join(deutsch))
    english.set("\n".join(englisch))
    
def show_all(root, event=None):
    global german
    global english
    update()
    showl1 = tk.Label(root, text="Deutsch:")
    showl1.grid(row=5, column=0, sticky="w", padx=5, pady=3)
    showl2 = tk.Label(root, textvariable=german)
    showl2.grid(row=6, column=0, sticky="w", padx=5, pady=3)
    showl3 = tk.Label(root, text="English")
    showl3.grid(row=5, column=1, sticky="w", padx=5, pady=3)
    showl4 = tk.Label(root, textvariable=english)
    showl4.grid(row=6, column=1, sticky="w", padx=5, pady=3)
    global b2
    b2.destroy()
    b2 = tk.Button(root, text="Hide", command=partial(show_nothing, showl1, showl2, showl3, showl4, root))
    b2.bind("<Return>", partial(show_nothing, showl1, showl2, showl3, showl4, root))
    b2.grid(row=4, column=1, sticky="w", padx=5, pady=3)


def show_nothing(label1, label2, label3, label4, root, event=None):
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    global b2
    b2 = tk.Button(root, text="Show all", command=partial(show_all, root))
    b2.bind("<Return>", partial(show_all, root))
    b2.grid(row=4, column=1, sticky="w", padx=5, pady=3)


def delete_entrys_window(root, event=None):
    delete = tk.Toplevel()
    delete.title("Delete Vocs")
    delete.focus_force()
    tk.Label(delete, text="Deutsch:").grid(row=0, column=0, sticky="w", padx=5, pady=3)
    tk.Label(delete, text="English:").grid(row=0, column=1, sticky="e", padx=5, pady=3)
    efile = open(directory + "/English.txt", "r+")
    dfile = open(directory + "/Deutsch.txt", "r+")
    x = 1
    for line in efile:
        tk.Label(delete, text=line.rstrip()).grid(row=x, column=1)
        delete.update()
        bn = tk.Button(delete, text="Delete", command=partial(delete_entrys, x))
        bn.bind("<Return>", partial(delete_entrys, x))
        bn.grid(row=x, column=2, sticky="w", padx=5, pady=3)
        x += 1
    x = 1
    for line in dfile:
        tk.Label(delete, text=line.rstrip()).grid(row=x, column=0)
        x += 1
    efile.close()
    dfile.close()
    root.update()
    delete.update()
    delete.mainloop()
    root.focus_force()
    e1.focus()


def delete_entrys(x, event=None):
    efile = open(directory + "\\English.txt", "w+")
    dfile = open(directory + "\\Deutsch.txt", "w+")
    print(efile.read())
    print(dfile.read())


def quit_window(root, event=None):
    root.quit()


if __name__ == "__main__":
    try:
        ask_window()
        print(chosen)
        if chosen is False:
            pass
        elif chosen is True:
            app()
    except NameError:
        pass
