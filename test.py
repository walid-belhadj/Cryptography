import random
a= random.randrange(2**256)
b= random.randrange(2**256)
from Crypto.Util import number
a = number.getPrime(256)

def nBitRandom(n):  
    return(random.randrange(2**(n-1)+1, 2**n-1)) 
print(a)
print("hexar de a est : " + hex(a))
print("bin de a est : " + bin(a))
#print(b)
# https://repl.it/@billbuchanan/getprimen
import Cyrpto.Util.number

import sys

bits=256

if (len(sys.argv)>1):
        bits=int(sys.argv[1])

print ("No of bits in prime is ",bits)

p=Crypto.Util.number.getPrime
(bits, randfunc=Crypto.Random.get_random_bytes)
print ("\nRandom n-bit Prime (p): ",p)
enc=pow(M,e,N)
print ("RSA Cipher(c=M^e mod N): ",enc)
dec = pow(enc,d,N)
print ("RSA Decipher (c^d mod N): ",dec)



from fastecdsa.curve import Curve
curve = Curve(
    name,  # (str): The name of the curve
    p,  # (long): The value of p in the curve equation.
    a,  # (long): The value of a in the curve equation.
    b,  # (long): The value of b in the curve equation.
    q,  # (long): The order of the base point of the curve.
    gx,  # (long): The x coordinate of the base point of the curve.
    gy,  # (long): The y coordinate of the base point of the curve.
    oid  # (str): The object identifier of the curve (optional).
)