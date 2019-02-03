import random

def give_prime():
    
    def isPrime(n):
        if(n>1):
            for i in range(2,n):
                if ((n%i)==0):
                    return False
                    break
                else:
                    return True
        else:
            return False
    
                
    def g_prime():
        primes=[i for i in range(1,9999) if isPrime(i)]
        n=random.choice(primes)
        return(n)
   
    s=g_prime()
    #print("First prime-->",s)
    return(s)

def secret_no():
    a=random.randint(1,9999)
    #print("Secret-->",a)
    return(a)

