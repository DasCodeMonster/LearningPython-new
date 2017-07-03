import socket


host = ""
port = 1337


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
print("Listening...")
connection, addr = s.accept()
print("Connected to " + addr)
path = input("Path of the file you want to send:\n")
file = open(path, "r").read().encode("utf-8")
connection.send(file)
print("File was sended succesfully!")
