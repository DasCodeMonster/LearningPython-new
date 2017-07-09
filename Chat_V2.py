import socket
import selectors
import threading
import msvcrt

sel = selectors.DefaultSelector()
Version = "0.0.3"
ProjectName = "MyChat"

con = False
stop = False


def myhelp():
    print("Commands:\n/help\n/create_room\n/leave_room\n/join_room\n/exit")


def test():
    try:
        global stop
        while True:
            if stop is True:
                break
            for key, mask in sel.select(timeout=1):
                if stop is True:
                    break
                callback = key.data
                callback(key.fileobj, mask)
    except OSError:
        print("Host closed the room")


def accept(insocket, mask):
    connection, addr = insocket.accept()
    print(addr, "joined your room")
    global addresses
    addresses.update({addr[0]: addr[1]})
    print(addresses)
    connection.setblocking(False)
    sel.register(connection, selectors.EVENT_READ, read)
    global con
    con = connection


def read(connection, mask):
    msg = connection.recv(1024)
    if msg:
        print(msg.decode("utf-8"))
    else:
        print("closing connection")
        print("Press <Enter> to continue")
        sel.unregister(connection)
        connection.close()


def create_room():
    global stop
    stop = False
    creator = True
    print("Create your room:")
    try:
        connections = int(input("Members: "))
        connections -= 1
    except ValueError:
        connections = 1
        print("Not a viable number of members. Number of members is set to 2")
    try:
        port = int(input("Port: "))
        connection = ("o.o.o.o", port)
    except ValueError:
        print("Port was not integer.Port is set to standard(1337)")
        connection = ("0.0.0.0", 1337)
    host_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_socket.bind(connection)
    host_socket.listen(connections)
    host_socket.setblocking(False)
    sel.register(host_socket, selectors.EVENT_READ, accept)
    threading.Thread(target=test).start()
    while True:
        if stop is True:
            break
        if con:
            send(con, creator)
            # send_neu(con)


def send(send_socket, creator):
    try:
        while True:
            msg = input()
            if msg.startswith("/"):
                command = msg.strip("/")
                if command == "leave_room":
                    leave_room()
                    send_socket.close()
                    break
                try:
                    commands[command]()
                except KeyError:
                    print("There is no command named", command)
            else:
                if creator is True:
                    global addresses
                    for key in addresses:
                        send_socket.send(msg.encode("utf-8"))
    except OSError:
        leave_room()
        pass


def send_neu(send_socket):
    try:
        while True:
            if msvcrt.kbhit():
                msg = msvcrt.getche().decode("ASCII")
                if msg.startswith("/"):
                    command = msg.strip("/")
                    if command == "leave_room":
                        leave_room()
                        send_socket.close()
                        break
                    try:
                        commands[command]()
                    except KeyError:
                        print("There is no command named", command)
                else:
                    send_socket.send(msg.encode("utf-8"))
    except OSError:
        leave_room()
        pass


def join_room(addr=None):
    # client_socket = None
    creator = False
    if addr:
        connection = (addr, 1337)
        client_socket = socket.create_connection(connection)
        client_socket.setblocking(False)
        sel.register(client_socket, selectors.EVENT_READ, read)
    else:
        connection = (socket.gethostbyname(socket.gethostname()), 1337)
        client_socket = socket.create_connection(connection)
        client_socket.setblocking(False)
        sel.register(client_socket, selectors.EVENT_READ, read)
    threading.Thread(target=test).start()
    send(client_socket, creator)
    # send_neu(client_socket)


def leave_room():
    global stop
    stop = True
    # print("set stop to True")


def get_own_address():
    print("Name:", socket.gethostname())
    print("IP-Address:", socket.gethostbyname(socket.gethostname()))


def save_shutdown():
    leave_room()
    exit()

addresses = {}
commands = {"help": myhelp, "create_room": create_room, "leave_room": leave_room, "join_room": join_room, "exit": exit,
            "address": get_own_address}

if __name__ == "__main__":
    print("Hello welcome to %s!\n Version: %s" % (ProjectName, Version))
    print("For help type /help.")
    while True:
        InRoom = False
        data = input("Command: ")
        if data.startswith("/"):
            data = data.strip("/")
            try:
                data = data.split(" ")
                try:
                    commands[data[0]](data[1])
                except KeyError:
                    print("There is no command named", data[0])
            except IndexError:
                try:
                    commands[data[0]]()
                except KeyError:
                    print("There is no command named", data[0])
