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
data=raw_input("Client2 ready to continue : yes/No: : ")
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
    
    
        
    digest=s.recv(1024)
    print "-----------------------------------------------------"
    print "-----------------DES PROCESS-------------------------"
    print "------------------------------------------------------"
    print "DECRYPTING THE MESSAGE using key ",Key
    cipher=s.recv(1024).decode()
    print "Cipher recieved from client is--------->",cipher
    print "Decrypting the cipher Text using the symmetric key....."
    BS=8
    PADDING='.'

    
    decipher=Des_Decrypt(Key,cipher)
        
    print "                        "
    
    print "Original Message is--------------->",decipher
    print "                        "
    
    print "---------------------------------------------------"
    print "------------CHECKING INTEGRITY---------------------"
    print "----------------------------------------------------"
    print "                        "
    
    print "Message digest recieved from client-->",s
    
    s2=hashing(decipher)
    print "calculated Hash value of recieved message---->",s2
    if(digest==s2):
        print "Integrity of message is intact ^-^  proceed forward...."
    else:
        print "Message is fabricated...... resend data................"
    print "__________________________________________________________________"
    data=raw_input("Do you wish to continue : : ")


    
    print "-----------------------------------------------------"
    print "-----------------DES ENCRYPTION-------------------------"
    print "------------------------------------------------------"
    print " "
    decipher=decipher.upper()
    print "Message to send client is---->",decipher
    print " "
    cipher=Des_Encrypt(Key,decipher)
    print "Cipher text of message ------- > ",cipher
    print " "
    
    s3=hashing(decipher)
    print "Hash of message-----> ",s3
    s.send(cipher)
    s.send(s3)
    
    
        
    
    
    data=raw_input("Do you wish to continue : : ")

s.close()
