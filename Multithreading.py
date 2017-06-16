import threading
import time

class MyThread(threading.Thread):
	Ergebnis = [0,1]
	Liste = []
	f = lambda z : z%2==0
	
	def __init__(self, ID, Name):
		threading.Thread.__init__(self)
		self.ID = ID
		self.Name = Name

	def runThread1(self):
		x = -1
		while True:
			x = x + 1
			self.Liste.append(x)
			if x == 200:
				break
			else:
				continue
				
	def runThread2(self):
		while len(self.Liste)<200:
			NeueListe = list(filter(self.f, self.Liste))
			print(NeueListe)
			
	def run(self, ID):
		# i=0
		# while i<20:
			# lockMe.acquire()
			# zahl = self.Ergebnis[len(self.Ergebnis)-2] + self.Ergebnis[len(self.Ergebnis)-1]
			# self.Ergebnis.append(zahl)
			# lockMe.release()
			# i = i+1
		if self.ID == 1:
			self.runThread1()
		else:
			self.runThread2()
			# x = -1
			# while True:
				# x = x + 1
				# self.Liste.append(x)
				# if x == 200:
					# break
				# else:
					# continue
		# else:
			# while len(self.Liste)<200:
				# NeueListe = list(filter(self.f, self.Liste))
				# print(NeueListe)
				
lockMe = threading.Lock()
Thread1 = MyThread(1, "Thread1")
Thread2 = MyThread(2, "Thread2")
Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
# print(MyThread.Ergebnis[42])

print("Beende Main Thread")