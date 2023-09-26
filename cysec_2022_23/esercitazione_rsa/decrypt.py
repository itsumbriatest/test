import hashlib
import rsa

with open('privkey.pem', 'rb') as p:
    s = p.read().decode("ascii")
    print(s)
    priv_key = rsa.PrivateKey._load_pkcs1_pem(s)

with open('pippo.enc', 'rb') as ciphertext_file:
    ciphertext = ciphertext_file.read()

cleartext = rsa.decrypt(ciphertext, priv_key)
m = hashlib.sha256()
m.update(cleartext)
print(m.hexdigest())

with open("pippo.dec", "wb") as pip:
    pip.write(cleartext)