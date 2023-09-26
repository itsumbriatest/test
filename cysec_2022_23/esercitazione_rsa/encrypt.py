import hashlib
import rsa

with open('pubkey.pem', 'rb') as p:
    pub_key = rsa.PublicKey.load_pkcs1_openssl_pem(p.read())

with open('pippo.txt', 'rb') as cleartext_file:
    cleartext = cleartext_file.read()

m = hashlib.sha256()
m.update(cleartext)
print(m.hexdigest())

encrypted = rsa.encrypt(cleartext, pub_key)
with open("pippo.enc", "wb") as out:
    out.write(encrypted)