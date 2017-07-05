import socket
import threading
import sys
# import select

Version = "0.0.3"
ProjectName = "MyChat"
connection = False
thread1 = False
thread2 = False
sock2 = False
exitVar = False
owner = False
joined = False
commands = ["help", "create_room", "leave_room", "join_room", "exit", "join_room_test"]


class Thread(threading.Thread):  # start a Thread to receive the msg
    def __init__(self, _id, task, host, port):
        threading.Thread.__init__(self)
        self.id = _id
        self.task = task
        self.host = host
        self.port = port

    def run(self):
        exec("self." + self.task + "()")

    def create(self):  # receive msg in own room
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # sock1.setblocking(0)
        sock1.bind((self.host, self.port))
        sock1.listen(1)
        global connection
        connection, addr = sock1.accept()
        # print(type(connection))
        global exitVar
        try:
            while True:
                if exitVar is True:
                    break
                else:
                    # print("in running thread", self.id)
                    # ready = select.select([sock1], [], [])
                    # print("meh")
                    # print(ready[0])
                    # if ready[0]:
                    #     msg = connection.recv(1024)
                    #     print(msg.decode("utf-8"))
                    msg = connection.recv(1024)
                    if msg.decode("utf-8").endswith("joined your room!"):
                        print("system:", msg.decode("utf-8"))
                    else:
                        print(msg.decode("utf-8"))
        except ConnectionAbortedError:
            global owner
            owner = False
            print("Thread ", self.id, " is finished")
        except ConnectionResetError:
            print("connectionreseterror")

    def joinRoom_alt(self):
        global sock2
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # sock2.setblocking(0)
        sock2.connect((self.host, self.port))
        # sock2.send(self.host.encode("utf-8") + " joined your room".encode("utf-8"))
        global exitVar
        while True:
            if exitVar is True:
                break
            else:
                # ready = select.select([sock2], [], [])
                # if ready[0]:
                #     msgIn = sock2.recv(1024)
                #     print(msgIn.decode("utf-8"))
                msgIn = sock2.recv(1024)
                print(msgIn.decode("utf-8"))

    def joinRoom(self):  # receive msg in joined room
        # print("in JoinRoom")
        global sock2
        sock2 = socket.create_connection((self.host, self.port))
        # print(sock2)
        try:
            try:
                while True:
                    # print("in loop")
                    msg = sock2.recv(1024)
                    if msg.decode("utf-8").startswith("/closeSocket"):
                        sock2.close()
                        print("break")
                        break
                    else:
                        print(msg.decode("utf-8"))
            except ConnectionResetError:
                print("connectionreseterror")
                sock2.close()
                global joined
                joined = False

            except ConnectionAbortedError:
                print("connectionabortederror")
                sock2.close()
                joined = False

        except TypeError:
            print("type error")
            sock2.close()
            # global joined
            joined = False
            print("thread finished")


def help():
    print("Commands:\n/help\n/create_room\n/leave_room\n/join_room\n/exit")


def exit():
    global exitVar
    exitVar = True
    global owner
    global joined
    global connection
    global sock2
    if owner is True:
        connection.send("/closeSocket".encode("utf-8"))
        connection.close()
        owner = False
        global thread1
        thread1.join()
    elif joined is True:
        sock2.send("/closeSocket".encode("utf-8"))
        sock2.close()
        joined = False
        global thread2
        thread2.join()
    sys.exit(0)


def create_room():  # create you own room
    host = ""
    port = 1337
    global thread1
    thread1 = Thread(1, "create", host, port)
    thread1.start()
    global connection
    global exitVar
    global owner
    owner = True
    try:
        while True:
            if exitVar is False:
                # msgout = input("Send: ")
                msgout = input()
                if msgout.startswith("/"):
                    command = msgout.strip("/")
                    if command in commands:
                        exec(command + "()")
                    else:
                        print("Not a command!")
                else:
                    if connection is not False:
                        connection.send(msgout.encode("utf-8"))
            else:
                connection.send("/closeSocket".encode("utf-8"))
                print("exit")
                connection.close()
                break
    except OSError:
        pass


def join_room():  # join an existing room
    host = socket.gethostbyname(socket.gethostname())
    # print(host)
    port = 1337
    global thread2
    thread2 = Thread(2, "joinRoom", host, port)
    thread2.start()
    global sock2
    while True:  # waiting for socket to init
        if sock2 is not False:
            break
        else:
            # print("waiting for socket")
            pass
    print("you joined a room")
    # print(sock2)
    sock2.send(host.encode("utf-8") + " joined your room!".encode("utf-8"))
    global exitVar
    global joined
    joined = True
    while True:
        if exitVar is not True or joined is not False:
            # msgout = input("Send: ")
            msgout = input()
            if msgout.startswith("/"):
                command = msgout.strip("/")
                if command in commands:
                    exec(command + "()")
                else:
                    print("Not a command!")
                    print(help())
            else:
                # print(sock2)
                if sock2 is not False:
                    # print("send!")
                    try:
                        sock2.send(msgout.encode("utf-8"))
                    except OSError:
                        break
        else:
            sock2.send("/closeSocket")
            sock2.close()
            print("finished")
            break
    sock2.close()
    print("end of join_room")

def join_room_test():
    host = "127.0.0.1"
    port = 1337
    testSock = socket.create_connection((host, port))
    while True:
        msg = testSock.recv(1024)
        print(msg.decode("utf-8"))


def leave_room():  # leave a room
    global owner
    global joined
    global connection
    global sock2
    if owner is True:
        connection.send("/closeSocket".encode("utf-8"))
        connection.close()
        owner = False
    elif joined is True:
        sock2.send("/closeSocket".encode("utf-8"))
        sock2.close()
        joined = False
    else:
        print("you are not in any room")

if __name__ == "__main__":  # start with commandline
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
