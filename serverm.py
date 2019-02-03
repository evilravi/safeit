import socket
import sys
import base64
import thread


from numbers_generations import give_prime, secret_no
from molding import calculate, hashing,Des_Encrypt,Des_Decrypt
from Crypto.Cipher import DES

MESSAGE=''
DIGEST=''
KEY=''


def multi_threading(c,a):
    while True:
        global MESSAGE
        global DIGEST
        global KEY
        print "                                       "
        print "Working with client1 Thread"
        print "                                        "
        d=c.recv(1024)
        b=c.recv(1024).decode()
    
    
        modulo=c.recv(1024).decode()
        print "-----------------------------------------------------"
        print "------------------SYMMETRIC KEY EXCHANGE------------------------"
        print "-----------------------------------------------------"
        secret=secret_no()
    
        print "Two prime numbers are--->",b," and ",modulo
    
    
        print "Bob Secret number is--->",secret
        print "Calculating Bob side.........."
        Bob=str(calculate(int(b),int(modulo),int(secret)))
        print "Bob calculated first value -->",Bob," Sending to Alice"
        c.send(Bob.encode())
        A=c.recv(1024).decode()

    
        print "Calulated value send by Alice is-->",A
    
        Key=calculate(int(A),int(modulo),int(secret))
        print "Bob is calculating key........"
        print "Key at Bob side is-------> ",Key
        Key=str(Key)
        KEY=Key


        s=c.recv(1024).decode()
        print "-----------------------------------------------------"
        print "-----------------DES PROCESS-------------------------"
        print "------------------------------------------------------"
        print "DECRYPTING THE MESSAGE using key ",Key
        cipher=c.recv(1024).decode()
        print "Cipher recieved from client is--------->",cipher
        print "Decrypting the cipher Text using the symmetric key....."
        BS=8
        PADDING='.'

    
        decipher=Des_Decrypt(Key,cipher)
        MESSAGE=decipher
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
        if(s==s2):
            print "Integrity of message is intact ^-^  proceed forward...."
        else:
            print "Message is fabricated...... resend data................"
        print "__________________________________________________________________"        
    
        DIGEST=s2
        print "                        "
        print "-------------REVERSE PROCESS--------------"
        if not d:
            break
        if "@No"==d.rstrip():
            break
    
    c.close()
    print a, "----terminates connection"

def multi_threading2(c,a):
    while True:
        global MESSAGE
        global DIGEST
        print "                                 "
        print "Working with client2 Thread"
        print "                                      "
        d=c.recv(1024)
        b=c.recv(1024).decode()
    
    
        modulo=c.recv(1024).decode()
        print "-----------------------------------------------------"
        print "------------------SYMMETRIC KEY EXCHANGE------------------------"
        print "-----------------------------------------------------"
        secret=secret_no()
    
        print "Two prime numbers are--->",b," and ",modulo
    
    
        print "Bob Secret number is--->",secret
        print "Calculating Bob side.........."
        Bob=str(calculate(int(b),int(modulo),int(secret)))
        print "Bob calculated first value -->",Bob," Sending to Alice"
        c.send(Bob.encode())
        A=c.recv(1024).decode()

    
        print "Calulated value send by Alice is-->",A
    
        Key=calculate(int(A),int(modulo),int(secret))
        print "Bob is calculating key........"
        print "Key at Bob side is-------> ",Key
        Key=str(Key)

        print "-----------------------------------------------------"
        print "------------------CALCULATE HASH  SHA256------------------------"
        print "-----------------------------------------------------"

        digest=hashing(MESSAGE)
        print "Calculated Hash value of message ----->",digest
        c.send(digest.encode())
        print "-----------------------------------------------------"
        print "--------------------DES ENCRYPTION------------------------"
        print "-----------------------------------------------------"


        cipher=Des_Encrypt(Key,MESSAGE)
        print "Cipher text is-------------->",cipher
        c.send(cipher.encode())
        print "                        "
        print "-------------REVERSE PROCESS--------------"
        print " "
        print "-----------------------------------------------------"
        print "--------------------DES DECRYPTION------------------------"
        print "-----------------------------------------------------"
        print " "
        print "DECRYPTING THE MESSAGE using key ",Key
        print " "
        cipher2=c.recv(1024).decode()
        digest2=c.recv(1024)
        print " "
        print "Cipher recieved from client is--------->",cipher2
        print " "
        print "Decrypting the cipher Text using the symmetric key....."
        print " "
        BS=8
        PADDING='.'
        MESSAGE=Des_Decrypt(Key,cipher2)
        print "Message send by client 2 is------> ",MESSAGE
        print " "
         
    
        print "---------------------------------------------------"
        print "------------CHECKING INTEGRITY---------------------"
        print "----------------------------------------------------"
        print "                        "
    
        print "Message digest recieved from client-->",digest2
    
        s3=hashing(MESSAGE)
        print "calculated Hash value of recieved message---->",s3
        if(digest2==s3):
            print "Integrity of message is intact ^-^  proceed forward...."
        else:
            print "Message is fabricated...... resend data................"
        print "__________________________________________________________________"        
        
        
        print "-----------------------------------------------------"
        print "--------------------DES ENCRYPTION------------------------"
        print "-----------------------------------------------------"


        cipher=Des_Encrypt(KEY,MESSAGE)
        print "Cipher text is-------------->",cipher
        print " "
        jump(cipher,c)
        
        

        print "-----------------------------------------------------"
        print "------------------CALCULATE HASH  SHA256------------------------"
        print "-----------------------------------------------------"

        digest3=hashing(MESSAGE)
        print "Calculated Hash value of message ----->",digest3
        jump(digest3,c)
        print " "
            
        
        if not d:
            break
        if "@No"==d.rstrip():
            break
    c.close()
    print a, "----terminates connection"

def jump(msg,c):
    for clients in list_of_clients:
        if clients!=c:
            clients.send(msg)
            
if __name__=='__main__':
    
        
    s=socket.socket()
    print("Welcome socket created-----")
    port=8888
    host='127.1.1.1'
    s.bind((host,port))
    print("Socket binded to ",port)
    list_of_clients=[]
    s.listen(2)
    count=0

    while True:
        print("Socket is listening----")
        c,addr=s.accept()
        list_of_clients.append(c)

    
        count=count+1
        print "--------------------------------------------------"
        print "Server connected to system having ip address --> ",addr
        if(count==1):
             thread.start_new_thread(multi_threading,(c,addr))
        else:
             thread.start_new_thread(multi_threading2,(c,addr))

