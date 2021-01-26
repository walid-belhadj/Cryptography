def vig_funct ( msg, cle, decode = False) :
    #definir un messqge et une clé 
    # decode ici joue le role de flqg: decode: False: crypte, True: décrypte
    msg_k = ""
    #vqriqble te,porqire
    for i,c in enumerate(msg) :
        #pqrcourir les lettres 
        d = cle[ i % len(cle) ]
        #d ttab takes the vqlues of key depending 
        #on the size of the msg 
        d = ord(d) - 65
        # convert and using ascii code 65=? 'a'
        if decode : d = 26 - d #26 nomre de lettre de l'alphabet
        msg_k += chr((ord(c)-65+d)%26+65)
    return msg_k

def DcdVig(msg, cle):
    return vig_funct (msg, cle, True)

def CdVig(msg, cle):
    return vig_funct (msg, cle)