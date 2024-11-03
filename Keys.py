from sympy import nextprime
from random import randint
from math import gcd

INDEXES = [1000,10000] #Smaller Primes used for proof of concept (Increased speed and less compute power needed) 
MAX_EXPONENT = 10000000


def findCoprimeValue(a, max_value):
    i = a
    while gcd(a,i) != 1:
        i = randint(0,max_value)  #Not the most effective method however due to using smaller values than normally used, effective enough
    
    return i

def createKeys():
    global INDEXES, MAX_EXPONENT
    #Generating Private Prime Keys
    prime_indexes = [randint(INDEXES[0],INDEXES[1]) for i in range(2)]
    private_keys = [nextprime(i) for i in prime_indexes]

    #Generating Public Keys
    public_mod_key = private_keys[0]*private_keys[1]
    eulers_value = public_mod_key - private_keys[0] - private_keys[1] + 1 #(p-1)(q-1). unnecessary use of compute power to calculate pq twice
    e = findCoprimeValue(eulers_value, MAX_EXPONENT)   #Chosen as to allow algorithm to run in reasonable amount of time
    
    return private_keys, [e,public_mod_key]

'''
private_key, public_key = createKeys()
print(private_key)
print(public_key)
'''