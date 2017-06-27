from Crypto.Cipher import AES
import base64
import random
import string
import sys


BLOCK_SIZE = 32
PADDING = "{"

pad =   lambda s: bytes(str(s) + (BLOCK_SIZE - len(str(s)) % BLOCK_SIZE ) * PADDING, "utf-8")
enc = lambda  c, m: base64.b64encode(c.encrypt(pad(m)))
dec = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)


def randomkey(byteanzahl):
    return bytes("".join(random.choice(string.ascii_letters + string.digits + "@#[]{}!@|$^?/&")
                         for i in range(byteanzahl)), "utf-8")


def randomName():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(3))


def randomAscii():
    return "".join(random.choice(string.ascii_letters) for i in range(3))


key = randomkey(32)
iv = randomkey(16) #Initialisierungsvektor

cipher = AES.new(key, AES.MODE_CBC, iv)

input = open("Neuanfang.py").readlines()
output = open("VokTrainer_encrypted.py", "w")

imports = list()
lines = list()

for line in input:
    if not line.startswith("#"):
        if "import" in line:
            imports.append(line.strip())
        else:
            lines.append(line)

enced = enc(cipher, bytes("".join(lines), "utf-8"))
b64name = randomAscii() + randomName()
aesName = randomAscii() + randomName()
imports.append("from base64 import b64decode as " + b64name)
imports.append("from Crypto.Cipher import AES as " + aesName)
random.shuffle(imports)
output.write(";".join(imports) + "\n")
cmd = "exec(%s.new(\"%s\", %s.MODE_CBC, \"%s\").decrypt(%s(\"%s\")).rstrip(\"{\"))\n" %(aesName, key, aesName, iv,
                                                                                        b64name, enced)
cmd = bytes(cmd, "utf8")
output.write("exec(%s(\"%s\"))" % (b64name, base64.b64encode(cmd)))
output.close()