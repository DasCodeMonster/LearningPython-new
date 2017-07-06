import socket
import sys
import selectors
import threading


commands = ["help", "create_room", "leave_room", "join_room", "exit", "join_room_test"]
sel = selectors.DefaultSelector()
Version = "0.0.3"
ProjectName = "MyChat"


def accept(socket, mask):
    connection, addr = socket.accept()
    print(addr, "joined your room")
    connection.setblocking(False)
    sel.register(connection, selectors.EVENT_READ, read)

def read(connection, mask):
    msg = connection.recv(1024)
    if msg:
        print(msg.decode("utf-8"))
    else:
        print("closeing", connection)
        sel.unregister(connection)
        connection.close()

def create_room():
    connection = ("", 1337)
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_socket.bind(connection)
    host_socket.listen(1)
    host_socket.setblocking(False)
    sel.register(host_socket, selectors.EVENT_READ, accept)
    send(host_socket)

def send(send_socket):
    while True:
        msg = input()
        if msg.startswith("/"):
            msg = msg.strip("/")
            if msg in commands:
                exec(data + "()")
            else:
                send_socket.send(msg.encode("utf-8"))

def join_room():
    connection = (socket.gethostbyname(socket.gethostname()), 1337)
    client_socket = socket.create_connection(connection)
    client_socket.setblocking(False)
    sel.register(client_socket, selectors.EVENT_READ, accept)
    send(client_socket)


if __name__ == "__main__":
    print("Hello welcome to %s!\n Version: %s" % (ProjectName, Version))
    print("For help type /help.")
    while True:
        InRoom = False
        data = input("Command: ")
        if data.startswith("/"):
            data = data.strip("/")
            if data in commands:
                exec(data + "()")
            else:
                print("There is no command named", data)
