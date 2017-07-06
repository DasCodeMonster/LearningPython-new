import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostname())
print()
httpserver = "www.youtube.com"
serveraddr = socket.gethostbyname(httpserver)
print(serveraddr, httpserver)
port = 80
my_socket.connect((serveraddr, port))
anfrage = "GET / HTTP/1.1\nHOST: " + httpserver + "\n\n"
my_socket.send(anfrage.encode("utf-8"))
data = ""
while True:
    dataencoded = my_socket.recv(1024)
    if not dataencoded:
        print("hi")
        break
    else:
        data = dataencoded.decode("iso-8859-1")
my_socket.close()
del my_socket
grenze = data.find("<")
if data == -1:
    print("Fegler bei der Übertragung")
else:
    print("HTTP-Overhead:\n" + "--------------\n" + data[:grenze-1] + "\n")
    print("HTTP-Inhalt:\n" + "--------------" + data[grenze:] + "\n")
