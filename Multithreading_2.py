import threading
import MultithreadingGUI
import tkinter as tk


class Thread(threading.Thread):
	def __init__(self, Id, Aufgabe):
		threading.Thread.__init__(self)
		self.Id = Id
		self.Aufgabe = Aufgabe

	def run(self):
		print("Thread", self.Id, "ist da")
		self.Aufgabe()


class Aufgaben():
	def Liste_erzeugen():
		for x in range(von, bis):
			t = threading.Thread(target=Aufgaben.Liste_sortieren, args=(x,))
			Liste.append(x)
			t.start()
		print(Liste)
		print(NeueListe)

	def Liste_sortieren(x):
		if x % teilen == 0:
			NeueListe.append(x)

	def Liste_filtern():
		pass

	def fib():
		i = 0
		while i < fibzahl + 1:
			lock.acquire()
			zahl = Fib[len(Fib) - 2] + Fib[len(Fib) - 1]
			Fib.append(zahl)
			lock.release()
			i = i + 1
		print("Thread 3 ist Fertig")

	def GUI():
		root = tk.Tk()
		w = tk.Label(root, text = NeueListe)
		w.pack()
		root.mainloop()

if __name__ == "__main__":
	while True:
		Liste = []
		NeueListe = []
		Fib = [0, 1]
		lock = threading.Lock()
		thread1finish = False
		thread2finish = False
		thread3finish = False

		while True:
			try:
				MultithreadingGUI()
				# fibzahl = int(input("Fibonaccizahl eingeben: "))
				fibzahl = int(MultithreadingGUI.e1.get())
				# von = int(input("Erstelle Liste von "))
				von = int(MultithreadingGUI.e2.get())
				# bis = int(input("bis ")) + 1
				bis = int(MultithreadingGUI.e3.get())
				# teilen = int(input("Liste teilen durch: "))
				teilen = int(MultithreadingGUI.e4.get())
				break
			except:
				print("Eingaben dürfen jeweils nur eine Zahl beinhalten!")

		Thread1 = Thread(1, Aufgaben.Liste_erzeugen)
		# Thread2 = Thread(2, Aufgaben.Liste_sortieren2)
		Thread3 = Thread(3, Aufgaben.fib)
		Thread3.start()
		# Thread2.start() #Thread1 und Thread2 tauschen!
		Thread1.start()
		Thread1.join()
		# Thread2.join()
		Thread3.join()
		ThreadGUI = Thread(4, Aufgaben.GUI())

		print("Die Fibonaccizahl von " + str(fibzahl) + " ist " + str(Fib[fibzahl]))
		print("\nZahlen, von " + str(von) + " bis " + str(bis - 1) + ", die durch " + str(teilen) + " Teilbar sind:\n" + str(NeueListe))

		Data1 = "Die Fibonaccizahl von " + str(fibzahl) + " ist " + str(Fib[fibzahl])
		Data2 = "\nZahlen, von " + str(von) + " bis " + str(bis - 1) + ", die durch " + str(teilen) + " Teilbar sind:\n" + str(NeueListe)
		Datainput = Data1 + Data2

		while True:
			Speichern = str(input("Speichern? (Ja/Nein): "))
			if Speichern == "Ja" or Speichern == "ja" or Speichern == "Yes" or Speichern == "yes" or Speichern == "Y" or Speichern == "y" or Speichern == "J" or Speichern == "j":
				fopen = open(str(input("Dateiname: ") + ".txt"), "w")
				fopen.write(Datainput)
				break

			elif Speichern == "Nein" or Speichern == "nein" or Speichern == "No" or Speichern == "no" or Speichern == "Nu" or Speichern == "nu" or Speichern == "N" or Speichern == "n" or Speichern == "Nay" or Speichern == "nay":
				break

			else:
				print("Ungültig\nNochmal...")
				continue

		nochmal = input("Neue Berechung? (Ja/Nein): ")
		if nochmal == "Ja" or nochmal == "ja" or nochmal == "J" or nochmal == "j" or nochmal == "Yes" or nochmal == "yes" or nochmal == "Y" or nochmal == "y":
			continue

		if nochmal == "Nein" or nochmal == "nein" or nochmal == "No" or nochmal == "no" or nochmal == "Nu" or nochmal == "nu" or nochmal == "N" or nochmal == "n" or nochmal == "Nay" or nochmal == "nay":
			print("Goodbye\nExit...")
			break