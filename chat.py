import socket
import threading


Version = "0.0.1"
ProjectName = "MyChat"
connection = False
thread1 = False
sock2 = False


class Thread(threading.Thread):
    def __init__(self, _id, task, host, port):
        threading.Thread.__init__(self)
        self.id = _id
        self.task = task
        self.host = host
        self.port = port

    def run(self):
        exec("self." + self.task + "()")

    def create(self):
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock1.bind((self.host, self.port))
        sock1.listen(1)
        global connection
        connection, addr = sock1.accept()
        print(type(connection))
        while True:
            msg = connection.recv(1024)
            print(msg.decode("utf-8"))

    def joinRoom(self):
        global sock2
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock2.connect((self.host, self.port))
        while True:
            msgIn = sock2.recv(1024)
            print(msgIn.decode("utf-8"))



def help():
    print("Commands:\n/help\n/create_room\n/leave_room\n/join_room\n/exit")


def exit():
    pass

def create_room():
    host = ""
    port = 1337
    global thread1
    thread1 = Thread(1, "create", host, port)
    thread1.start()
    InRoom = True
    global connection
    while True:
        msgout = input("Send: ")
        if msgout.startswith("/"):
            command = msgout.strip("/")
            if command in commands:
                exec(command + "()")
        else:
            if connection is not False:
                connection.send(msgout.encode("utf-8"))


def join_room():
    host = "127.0.0.1"
    port = 1337
    thread2 = Thread(2, "joinRoom", host, port)
    thread2.start()
    global sock2
    sock2.send(host.encode("utf-8") + " joined your room".encode("utf-8"))
    print("you joined a room")
    while True:
        msgout = input("Send: ")
        if msgout.startswith("/"):
            command = msgout.strip("/")
            if command in commands:
                exec(command + "()")
        else:
            if sock2 is not False:
                sock2.send(msgout.encode("utf-8"))


commands = ["help", "create_room", "leave_room", "join_room", "exit"]
print("Hello welcome to %s!\n Version: %s" %(ProjectName, Version))
print("For help type /help.")
while True:
    InRoom = False
    data = input("Command: ")
    if data.startswith("/"):
        data = data.strip("/")
        if data in commands:
            exec(data + "()")
        else:
            print("There is no command named ", data)
