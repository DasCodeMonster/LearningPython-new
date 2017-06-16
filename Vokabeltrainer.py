class Entry:
	def __init__(self, deutsch, englisch, tipp):
		self.deutsch = deutsch
		self.englisch = english

def eingabe():
	print("Eingabe")

def abfrage():
	print()

def printall():
	print("printall")
	
einträge = []

if __name__ == "__main__":
	while True:
	# try:
		tipp = "Tipp"
		befehl = str(input("Befehl: "))
		# if befehl == "Eingabe" or "eingabe" or "new entry":
			# eingabe()
			# break
		if befehl == "Abfrage":
			# abfrage()
			print("Fail")
		# elif befehl == "Beenden" or "exit" or "beenden" or "Exit":
			# break
		elif befehl == "Ausgabe" or "printall":
			# printall()
			print("Fail02")
		elif befehl == "Help" or "help" or "hilfe" or "Hilfe":
			print("""Benutze "Eingabe", um eine neue Vokabel hinzuzufügen,"Abfrage", um dich Abfragen zu lassen,
			"Ausgabe", um alle Vokabeln auszugeben und "Beenden", um das Programm zu beenden.""")
		elif befehl == "Tipp" or "tipp":
			print(tipp)
		else:
			print("Keine gültige Anweisung. Bitte erneut Befehl eingeben.")
	# except NameError:
		# print("NameError")
		# continue
	# except TypeError:
		# print("TypeError")
		# continue