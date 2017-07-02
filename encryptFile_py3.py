from Crypto.Cipher import AES
import base64
import random
import string


BLOCK_SIZE = 32
PADDING = "{"

pad = lambda s: str(s) + (BLOCK_SIZE - len(str(s)) % BLOCK_SIZE ) * PADDING
enc = lambda  c, m: base64.b64encode(c.encrypt(pad(m).encode()))
dec = lambda c, e: c.decrypt(base64.b64decode(e)).decode().rstrip(PADDING)

def randomkey(byteanzahl):
    return bytes("".join(random.choice(string.ascii_letters + string.digits + "@#[]{}!@|$^?/&")
                         for _ in range(byteanzahl)), "utf-8")

def randomName():
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(3))


def randomAscii():
    return "".join(random.choice(string.ascii_letters) for _ in range(3))

key = randomkey(32)
iv = randomkey(16) #Initialisierungsvektor

# cipher = AES.new(key, AES.MODE_ECB, iv)
cipher = AES.new(key, AES.MODE_OFB, iv)


# encrypted = cipher.encrypt("Hello World aaaa".encode())
# print(encrypted)
# decrypted = cipher.decrypt(encrypted)
# print(decrypted.decode())


input = open("VokTrainer.py").readlines()
output = open("VokTrainer_encrypted.py", "w")
# output = open("Test_env.py", "w")
 
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

cmd = "exec(%s.new(\"%s\".encode(), %s.MODE_OFB, \"%s\".encode()).decrypt(%s(\"%s\".encode())).decode().rstrip(\"{\"))\n" %(aesName, key.decode(), aesName, iv.decode(), b64name, enced.decode())
 
output.write("exec({}(\"{}\".encode()))".format(b64name, base64.b64encode(cmd.encode()).decode()))
output.close()