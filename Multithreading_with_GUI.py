import threading
import tkinter.filedialog as tkf
import tkinter as tk
from functools import partial

lock = threading.Lock()

class Thread(threading.Thread):
    def __init__(self, Id, Aufgabe, args=()):
        threading.Thread.__init__(self)
        self.Id = Id
        self.Aufgabe = Aufgabe
        self.args=args

    def run(self):
        print("Thread", self.Id, "ist da")
        self.Aufgabe(*self.args)


class Aufgaben():
    def Liste_erzeugen(von, bis, teilen):
        Liste = []
        global NeueListe
        NeueListe = []
        for x in range(von, bis):
            t = threading.Thread(target=Aufgaben.Liste_sortieren, args=(x,teilen, NeueListe,))
            Liste.append(x)
            t.start()
        print("Thread 1 ist fertig")
        print(Liste)

    def Liste_sortieren(x, teilen, NeueListe):
        if x % teilen == 0:
            NeueListe.append(x)
            print(NeueListe)

    def fib(fibzahl, Fib):
        i = 0
        while i < fibzahl + 1:
            lock.acquire()
            zahl = Fib[len(Fib) - 2] + Fib[len(Fib) - 1]
            Fib.append(zahl)
            lock.release()
            i = i + 1
        print("Thread 3 ist Fertig")

def app():
    root = tk.Tk()
    root.title("Multithreading GUI")
<<<<<<< HEAD
=======
    root.iconbitmap("D:\\PythonProject\\Logo.scale-100.png")
>>>>>>> 773330924b6ed7d3fca06794f6c61c3daa555281
    menu = tk.Menu(root)
    root.config(menu=menu)
    Helpmenu = tk.Menu(menu)
    menu.add_cascade(label="Help", menu=Helpmenu)
    tk.Label(root, text="Stelle der Fibonaccizahl:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    e1_fibzahl = tk.Entry(root)
    e1_fibzahl.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    tk.Label(root, text="Fibonaccizahl der Stelle X:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
<<<<<<< HEAD
    tk.Label(root, text="Hier steht die Fibonaccizahl").grid(row=1, column=1, sticky="w", padx=5, pady=5)
=======
    global fib_ergebnis
    fib_ergebnis = tk.StringVar()
    tk.Label(root, textvariable=fib_ergebnis).grid(row=1, column=1, sticky="w", padx=5, pady=5)
>>>>>>> 773330924b6ed7d3fca06794f6c61c3daa555281
    tk.Label(root, text="Liste Sortieren:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    tk.Label(root, text="Start Liste:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    e2_von = tk.Entry(root)
    e2_von.grid(row=3, column=1, sticky="w", padx=5, pady=5)
    tk.Label(root, text="EndeListe").grid(row=4, column=0, sticky="w", padx=5, pady=5)
    e3_bis = tk.Entry(root)
    e3_bis.grid(row=4, column=1, sticky="w", padx=5, pady=5)
    tk.Label(root, text="Zahlen in Liste, die durch n Teilbar sind: n=").grid(row=5, column=0, sticky="w", padx=5, pady=5)
    e4_teilen = tk.Entry(root)
    e4_teilen.grid(row=5, column=1, sticky="w", padx=5, pady=5)
    tk.Label(root, text="Ergebnis:").grid(row=6, column=0, sticky="w", padx=5, pady=5)
<<<<<<< HEAD
    tk.Label(root, text="Hier steht die Liste").grid(row=6, column=1, sticky="w", padx=5, pady=5)
    tk.Button(root, text="Quit", command=root.quit).grid(row=7, column=0, sticky="w", padx=5, pady=5)
    Datainput = tk.StringVar()
    Datainput.set(get_entrys)
    tk.Button(root, text="Berechnen", command=partial(Berechnen, e1_fibzahl, e2_von, e3_bis, e4_teilen, Datainput)).grid(row=7, column=0, sticky="ne", padx=5, pady=5)
    tk.Button(root, text="Save", command=partial(Speichern, Datainput)).grid(row=7, column=1, sticky="e", padx=5, pady=5)
=======
    global liste_ergebnis
    liste_ergebnis = tk.StringVar()
    tk.Label(root, textvariable=liste_ergebnis).grid(row=6, column=1, sticky="w", padx=5, pady=5)
    b1 = tk.Button(root, text="Quit", command=partial(quit, root))
    b1.bind("<Return>", partial(quit, root))
    b1.grid(row=7, column=0, sticky="w", padx=5, pady=5)
    b2 = tk.Button(root, text="Berechnen", command=partial(Berechnen, e1_fibzahl, e2_von, e3_bis, e4_teilen))
    b2.bind("<Return>", partial(Berechnen, e1_fibzahl, e2_von, e3_bis, e4_teilen    ))
    b2.grid(row=7, column=0, sticky="ne", padx=5, pady=5)
    b3 = tk.Button(root, text="Save", command=Speichern)
    b3.bind("<Return>", Speichern)
    b3.grid(row=7, column=1, sticky="e", padx=5, pady=5)
>>>>>>> 773330924b6ed7d3fca06794f6c61c3daa555281
    root.mainloop()

def get_entrys(e1_fibzahl, e2_von, e3_bis, e4_teilen):
    fibzahl = int(e1_fibzahl.get())
    von = int(e2_von.get())
    bis = int(e3_bis.get()) + 1
    teilen = int(e4_teilen.get())
<<<<<<< HEAD
    return fibzahl, von, bis, teilen

def Berechnen(e1_fibzahl, e2_von, e3_bis, e4_teilen, Datainput):
    fibzahl, von, bis, teilen =  get_entrys(e1_fibzahl, e2_von, e3_bis, e4_teilen)
    Thread1 = Thread(1, Aufgaben.Liste_erzeugen, args=(von, bis, teilen,))
    Thread3 = Thread(3, Aufgaben.fib, args=(fibzahl,))
    Thread3.start()
=======
    # if int(bis) > int(von):
    #     bis = int(e2_von.get())
    #     von = int(e3_bis.get())
    event = ""
    return fibzahl, von, bis, teilen, event

def Berechnen(e1_fibzahl, e2_von, e3_bis, e4_teilen, event):
    Fib = [0, 1]
    fibzahl, von, bis, teilen, event =  get_entrys(e1_fibzahl, e2_von, e3_bis, e4_teilen)
    Thread1 = Thread(1, Aufgaben.Liste_erzeugen, args=(von, bis, teilen,))
    Thread3 = Thread(3, Aufgaben.fib, args=(fibzahl, Fib,))
>>>>>>> 773330924b6ed7d3fca06794f6c61c3daa555281
    Thread1.start()
    Thread3.start()
    Thread1.join()
    Thread3.join()
<<<<<<< HEAD
    Data = "Die Fibonaccizahl von " + str(fibzahl) + " ist " + str(Fib[fibzahl]) + "\nZahlen, von " + str(von) + " bis " + str(bis - 1) + ", die durch " + str(teilen) + " Teilbar sind:\n" + str(NeueListe)
    print(Data)
    Datainput = Data



def Speichern(getdata):
    directory = tkf.asksaveasfile("w", defaultextension=".txt")
    directory.write(getdata)
=======
    fib_ergebnis.set(Fib[fibzahl])
    liste_ergebnis.set(NeueListe)
    global Data
    Data = "Die Fibonaccizahl von " + str(fibzahl) + " ist " + str(Fib[fibzahl]) + "\nZahlen, von " + str(von) + " bis " + str(bis - 1) + ", die durch " + str(teilen) + " Teilbar sind:\n" + str(NeueListe)
    print(Data)


def Speichern(event):
    directory = tkf.asksaveasfile("w", defaultextension=".txt")
    directory.write(Data)
>>>>>>> 773330924b6ed7d3fca06794f6c61c3daa555281
    directory.close()

def quit(root, event):
    root.quit()

if __name__ == "__main__":
<<<<<<< HEAD
    Liste = []
    NeueListe = []
    Fib = [0, 1]
    lock = threading.Lock()
=======
>>>>>>> 773330924b6ed7d3fca06794f6c61c3daa555281
    app()