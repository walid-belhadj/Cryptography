from Crypto.Util import number
import random
import hashlib	
import hashlib
mystring = input('Enter String to hash: ')
hash_object = hashlib.sha256(mystring.encode())
print(hash_object.hexdigest())
a = number.getPrime(256)
b = number.getPrime(256)
_G = number.getPrime(256)
_P = number.getPrime(256)
a= random.randrange(2**256)

#clacule pgcd 
def gcd(a,b):
    a,b=(b,a) if a<b else (a,b)
    while b:
        a,b=b,a%b
    return a
# Extended Euclidean Algorithm,  returns x, y, gcd(a,b) such that ax + by = gcd(a,b)
def egcd(a,b):
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u, v, a
    
#prime number
def isprime(n):
    #check if n is prime  100 times
    for q in range(100):
        a = random.randint(2,n-1)
        if pow(a, n - 1, n) != 1:
            return 0
    return 1

def build_ec(a=1, b=1, n_bits=4):
    #check our discriminant
    disc = 4 * pow(a, 3) + 27 * pow(b, 2)
    if disc == 0:
        return (-1,-1,-1)
    #our prime q should be n_bits and q mod 4 should equal 3 for this system
    q = prime_maker(n_bits)
    while q %  4 == 1:
        q = prime_maker(n_bits)
    #generate a prime that q mod 4 = 3
    return (a, b, q)
