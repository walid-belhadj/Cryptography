from random import randint
from fractions import gcd
from modtools import *

#génération des clés 

def gen_key(n):
    w = [randint(1, 99)]
    #génération des chiffres pseudoaléatoire entre 1 et 99 
    multp = randint(2, 49)
#générer les ,uliplicateurs q1, q2, q3.....qn
    for i in range(n - 1):
        w += [randint(sum(w), multp*sum(w))]


    q = randint(sum(w), multp*sum(w))
    r = randint(1, q)

    while pgcd(q, r) != 1:
        r = randint(0, q)

    B = [(w[i] * r) % q for i in range(len(w))]
    # retourner lq cle publique
    
    return B, w, q, r

    #fonction de chiffrement 
def encrypt(m, B):
    return sum([m[i] * B[i] for i in range(len(m))])
    #retourner la somme de la 

def binarize(m):
    return [int(i) for i in "{:08b}".format(m)]


def decrypt(c, w, r, q):
    text = [0]*len(w)
    ctext = (c * modinv(r, q)) % q

    while(ctext > 0):
        y = max(x for x in w if x <= ctext)
        ctext -= y
        text[w.index(y)] = 1

    return text

if __name__ == "__main__":
    B, w, q, r = gen_keys(8)
    m = binarize(97)
    c = encrypt(m, B)
    p = decrypt(c, w, r, q)
    print(c, p)