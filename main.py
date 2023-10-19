import rsa

def load_keys():
    with open('keys/pubkey.pem','rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem','rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())
    
    return pubKey,privKey

def encrypt(msg,key):
    return rsa.encrypt(msg.encode(),key)

def decrypt(ciphertext,key):
    try:
        return rsa.decrypt(ciphertext,key).decode()
    except:
        return False

pubKey, privKey = load_keys()


