class Lebewesen:
	Augen=2
class Hund(Lebewesen):
	Beine=4
	Name="Doge"
	#def __init__(self,):
	def NeueAugen(self,Augenanzahl):
		self.Augen=Augenanzahl
Doge = Hund()
i = input("Wie heißt das Lebewesen?: ")
f = open(i,"w")
f.write(i + "\n")
f.close
i2 = input("Hat das Lebewesen 2 Augen?(Ja/Nein): ")
if i2 == "Ja":
	f = open(i,"a")
	f.write("Augen: 2\n")
	f.close
elif i2 == "Nein":
	i2 = input("Gebe die Anzahl der Augen ein: ")
	i2 = int(i2)
	Doge.NeueAugen(i2)
	f = open(i, "a")
	f.write("Augen: " + i2)
print("Datei gespeichert unter: C:\\Users\\Philip\\Desktop\\Git_Python\\",i)