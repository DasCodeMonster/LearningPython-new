# import time
# if __name__ == "__main__":
# 	# f=open("D:\\PythonProject\\Bio.txt","w+")
# 	# #print(f.read())
# 	# #print(f.readline())
# 	# a=input("Name: ")
# 	# a="Name: "+a
# 	# f.write(a)
# 	# b=input("Alter: ")
# 	# b="\nAlter: "+b
# 	# f.write(b)
# 	# c=input("Geburtsdatum: ")
# 	# c="\nGeburtsdatum: "+c
# 	# f.write(c)
# 	# time.sleep(1)
# 	# print(f.read())
# 	# f.close
# 	# time.sleep(3)
# 	rf = open("D:\\PythonProject\\Bio.txt","r+")
# 	print(rf.readlines())
# 	rf.close
f = open("D:\\Test.txt", "r")
# f.writelines("Zeile 1")
# f.writelines("\n")
# f.writelines("Zeile 2\n")
# f.writelines("Zeile 3")
# f.write("\nZeile 4")
# f.close()
# print(f.read())
Zeilen = []
for line in f:
	# print(line.rstrip())
	Zeilen.append(line.rstrip())

print(Zeilen[2])
