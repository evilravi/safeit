from Crypto.Hash import SHA256
from Crypto.Cipher import DES
import base64

def calculate(base,modulo,s):
    send=((base**s)%modulo)    
    return(send)

def hashing(sentence):
    
    d=SHA256.new()
    d.update(sentence)
    digest=d.hexdigest()
    return digest

def Des_Encrypt(Key,plain):
    print "ENCRYPTING THE MESSAGE using key ",Key
    BS=8
    PADDING='.'

    pad=lambda k: k+(BS-len(k)%BS)*PADDING
    new_s=pad(plain)
    obj=DES.new(pad(Key),DES.MODE_ECB)
    cipher=base64.b64encode(obj.encrypt(pad(new_s)))
    return cipher

def Des_Decrypt(Key,cipher):
    BS=8
    PADDING='.'

    pad=lambda k: k+(BS-len(k)%BS)*PADDING
    obj=DES.new(pad(Key),DES.MODE_ECB)
    decipher=obj.decrypt(base64.b64decode(cipher)).rstrip(PADDING)
    return decipher
