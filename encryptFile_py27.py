from Crypto.Cipher import AES
import base64
import random
import string


BLOCK_SIZE = 32
PADDING = "{"

pad = lambda s: str(s) + (BLOCK_SIZE - len(str(s)) % BLOCK_SIZE ) * PADDING
enc = lambda c, m: base64.b64encode(c.encrypt(pad(m)))
dec = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)


def randomkey(byteanzahl):
    return "".join(random.choice(string.ascii_letters + string.digits + "@#[]{}!@|$^?/&")
                         for i in range(byteanzahl))


def randomName():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(3))


def randomAscii():
    return "".join(random.choice(string.ascii_letters) for i in range(3))


key = randomkey(32)
iv = randomkey(16)  # Initialisierungsvektor

cipher = AES.new(key, AES.MODE_CBC, iv)

input = open("C:\\Users\\Philip\\Desktop\\Python_Git\\Neuanfang.py").readlines()
# output = open("VokTrainer_encrypted.py", "w")
output = open("C:\\Users\\Philip\\Desktop\\Python_Git\\Neuanfang_encrypted.py", "w")

imports = list()
lines = list()

for line in input:
    if not line.startswith("#"):
        if "import" in line:
            imports.append(line.strip())
        else:
            lines.append(line)

enced = enc(cipher, "".join(lines))
b64name = randomAscii() + randomName()
aesName = randomAscii() + randomName()
imports.append("from base64 import b64decode as " + b64name)
imports.append("from Crypto.Cipher import AES as " + aesName)
random.shuffle(imports)
output.write(";".join(imports) + "\n")
cmd = "exec(%s.new(\"%s\", %s.MODE_CBC, \"%s\").decrypt(%s(\"%s\")).rstrip(\"{\"))\n" %(aesName, key, aesName, iv,
                                                                                        b64name, enced)
output.write("exec(%s(\"%s\"))" % (b64name, base64.b64encode(cmd)))
output.close()