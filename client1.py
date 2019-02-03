from numbers_generations import give_prime, secret_no
from molding import calculate, hashing,Des_Encrypt,Des_Decrypt
from Crypto.Cipher import DES
import base64

import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Client Socket created-------------"
port=8888
ip='127.1.1.1'
s.connect((ip,port))
data=raw_input("Client1 ready to continue : yes/No: : ")
while data!="@No":
    s.send(data)
    b=str(give_prime())
    modulo=str(give_prime())
    print "-----------------------------------------------------"
    print "------------------SYMMETRIC KEY EXCHANGE------------------------"
    print "-----------------------------------------------------"

    print "Two prime numbers are--->",b," and ",modulo
    secret=secret_no()
    print "Alice Secret number is--->",secret
    s.send(b.encode())
    s.send(modulo.encode())

    Alice=str(calculate(int(b),int(modulo),int(secret)))
    print "Calculating Alice side.........."
    print "Alice calculated first value -->",Alice," Sending to Server"
    s.send(Alice.encode())
    B=s.recv(1024).decode()
    print "Calulated value send by Bob is-->",B
    Key=calculate(int(B),int(modulo),int(secret))
    print "Alice is calculating key........"
    print "Key of Alice is--------->",Key
    Key=str(Key)

    sentence=raw_input("Input the message : : ")
    print "-----------------------------------------------------"
    print "------------------CALCULATE HASH  SHA256------------------------"
    print "-----------------------------------------------------"

    digest=hashing(sentence)
    print "Calculated Hash value of message ----->",digest
    s.send(digest.encode())
    print "-----------------------------------------------------"
    print "--------------------DES ENCRYPTION------------------------"
    print "-----------------------------------------------------"


    cipher=Des_Encrypt(Key,sentence)
    print "Cipher text is-------------->",cipher
    s.send(cipher.encode())
    print " "
    print "--------------Waiting for Message to arrive ---------------"
    print " "
    print "-----------------------------------------------------"
    print "--------------------DES DECRYPTION------------------------"
    print "-----------------------------------------------------"

    cipher=s.recv(1024)
    digest2=s.recv(1024)
    decipher=Des_Decrypt(Key,cipher)
    print "Cipher text received is-------------->",cipher
    print " "
    print "Decrypted Message is -----------------> ",decipher
    print " "
    print "---------------------------------------------------"
    print "------------CHECKING INTEGRITY---------------------"
    print "----------------------------------------------------"
    print "                        "
    
    print "Message digest recieved from client-->",digest2
    print " "
    
    s3=hashing(decipher)
    print "calculated Hash value of recieved message---->",s3
    if(digest2==s3):
        print "Integrity of message is intact ^-^  proceed forward...."
    else:
        print "Message is fabricated...... resend data................"
    print "__________________________________________________________________"        
        
    
    
    
    data=raw_input("Do you wish to continue : : ")

s.close()
