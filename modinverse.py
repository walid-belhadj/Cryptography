#prime number 
Pcurve = 97  # The proven prime
#nombre de point dans le coprs
N=0xFFF0 # Number of points in the field
Acurve = 1; Bcurve = 6
 #  a et b de lequatino usuelleThese two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
#points generateurs
Gx = 25
Gy = 18
GPoint = (Gx,Gy) # This is our generator point. Trillions of dif ones possible
#Individual Transaction/Personal Information own pirvte key
privKey = 0x1111
##def des fonctions
def modinv(a,n): #Extended Euclidean Algorithm/'division' in elliptic curves
# a = 10^-1 mod n = 17
    a = a % n
    for x in range(1,n):
    	if ((a*x) % n == 1):
    		return x
    return 1
    ####
def ECadd(a,b): # Not true addition, fist case x1 != x2 invented for EC. Could have been called anything.
    #LamAdd , b[1] = y2 , a[1]= y1 
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) % Pcurve
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
    return (x,y)
######
def ECdouble(a): # This is called point doubling, also invented for EC.
    Lam = ((3*a[0]*a[0]+Acurve) * modinv((2*a[1]),Pcurve)) % Pcurve
    x = (Lam*Lam-2*a[0]) % Pcurve
    y = (Lam*(a[0]-x)-a[1]) % Pcurve
    return (x,y)
###########
def EccMultiply(GenPoint,ScalarHex): #Double & add. Not true multiplication
    #check si le prvt key est 0 ou point generatuer est 0 
    #t point generateur doit etre petit que N defini au debut 
	    if ScalarHex == 0 or ScalarHex >= N: raise Exception("Invalid Scalar/Private Key")
	    #we use double and addd (wiki) sqrt and multi 
	    ScalarBin = str(bin(ScalarHex))[2:] # from pos 2 exdl till the end
	    #on itere et a chaque point du ec on regarde combien 
	    # d'add point or doubling to get your final out put 
	    Q=GenPoint
	    for i in range (1, len(ScalarBin)): # 256 bit binary This is invented EC multiplication.
	        Q=ECdouble(Q); #print "DUB", Q[0]; print #always doing doubling here
	        if ScalarBin[i] == "1": #move to the second charct
	            Q=ECadd(Q,GenPoint); # print "ADD", Q[0]; print #print dbl
	    return (Q)#return the privt key 
print  ("******* Public Key Generation *********")
print
PublicKey = EccMultiply(GPoint,privKey)
print ("the private key:"); 
print (privKey); print
print ("the uncompressed public key (not address):"); 
print (PublicKey); print
print ("the uncompressed public key (HEX):"); 
print  ("04" + "%064x" % PublicKey[0] + "%064x" % PublicKey[1]); 
print;
print ("the official Public Key - compressed:"); 
if PublicKey[1] % 2 == 1: # If the Y value for the Public Key is odd.
    print ("03"+str(hex(PublicKey[0])[2:-1]).zfill(64))
else: # Or else, if the Y value is even.
    print ("02"+str(hex(PublicKey[0])[2:-1]).zfill(64))
#NPcurve = int(input("enter la base N, mod N exp: "))
##ax= int(input("enter a number to find inverse a^-1 exp "))
#print ("ax inversemod NPcurve: "+str(modinv(ax,NPcurve)))
  ###


