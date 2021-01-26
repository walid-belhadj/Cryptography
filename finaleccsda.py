from Crypto.Util import number
import random
import hashlib	
print("**************ECDSA Signature****************")
print("Enter the  curve elements y^2=x^3+ a * x + b ")
aC=int(input("enter the value of a; "))
bC=int(input("enter the value of b; "))
Pcurve=int(input("enter the value of P (prime); "))
print("please enter the generatic point coordonates Xg, Yg of the curve")
kscal = random.randrange(99)
N = random.randrange(100,200)
private_key= 
xG=int(input("enter the value of Xg; "))
yG=int(input("enter the value of Xg; "))
GPoint = (xG,yG) # This is our generator point. Trillions of dif ones possible
#Calculer Q = h G =(x​ 1​ , y​ 1​ )

#Calculer r= x​ 1​ mod n.
r = xG%N
#k= k​ -1​ mod n.
kTmp = modinv(kscal,N)
#compute the hash 
mystring = input('Enter String to hash: ')
hash_object = hashlib.sha256(mystring.encode())
print(hash_object.hexdigest())
#● Calculer s = k​ -1​ (e + ​ x ​ A r) mod n
sig = kTmp * (mystring+ private_key*r)% N

#Vérification de la signature par Bob
#● Calculer w = s​ -1​ mod n
w = modinv(s, N)

#● Calculer e=HASH(m)

#● Calculer u​ 1​ = e w mod n et u​ 2​ = r w mod n
u1 = ( e * w ) % N
u1 = ( r * w ) % N
#● Calculer (x​ 1​ , y​ 1​ ) = u​ 1 G + u​ 2​ Q

La signature est validée si r=x​ 1​ mod n
	#prime number
	def isprime(n):
	    #check if n is prime  100 times
	    for q in range(100):
	        a = random.randint(2,n-1)
	        if pow(a, n - 1, n) != 1:
	            return 0
	    return 1
	#Extended Euclid/ in EC
	def modinv(a,n): # a = 10^-1 mod n = 17
	    a = a % n
	    for x in range(1,n):
	    	if ((a*x) % n == 1):
	    		return x
	    return 1
	# Return true if point GPoint lies on our curve
		def touches(self,GPoint):
			yTmp=(yG*yG)%self.Pcurve
			xTmp=(self.field_mul((xG*xG)%self.Pcurve
				+self.aC,xG)+self.bC)%self.Pcurve
			return yTmp==(xTmp)%self.Pcurve

	def EccMultiply(GenPoint,kscal): #Double & add. Not true multiplication
	    #check si le prvt key est 0 ou point generatuer est 0 
	    #t point generateur doit etre petit que N defini au debut 
	    if kscal == 0 or kscal >= N: raise Exception("Invalid Scalar/Private Key")
	    #we use double and addd (wiki) sqrt and multi 
	    kscalbin = str(bin(kscal))[2:] # from pos 2 exdl till the end
	    #on itere et a chaque point du ec on regarde combien 
	    # d'add point or doubling to get your final out put 
	    Q=GenPoint
	    for i in range (1, len(kscalbin)): # 256 bit binary This is invented EC multiplication.
	        Q=ECdouble(Q); #print "DUB", Q[0]; print #always doing doubling here
	        if kscalbin[i] == "1": #move to the second charct
	            Q=ECadd(Q,GenPoint); # print "ADD", Q[0]; print #print dbl
	    return (Q)#return the privt key 
# An elliptic curve has these fields:
#   p: the prime used to mod all coordinates
#   a: linear part of curve: y^2 = x^3 + ax + b
#   b: constant part of curve
#   G: a curve point (G.x,G.y) used as a "generator"
#   n: the order of the generator
def __init__(self, aC, bC, Pcurve):
		self.aC = aC
		self.bC = bC
		self.Pcurve = Pcurve
		self.points = []
		self.define_points()


	def define_points(self):
		self.points.append(INF_POINT)
		for x in range(self.Pcurve):
			for y in range(self.Pcurve):
				if self.equal_modp(y * y, x * x * x + self.aC * x + self.bC):
					self.points.append((x,y))	

	# Prime field multiplication: return a*b mod p
	def field_mul(self,a,b):
		return (a*b)%self.Pcurve

	# Prime field division: return num/den mod p
	def field_div(self,num,den):
		inverse_den=modinv(den%self.Pcurve,self.Pcurve)
		return self.field_mul(num%self.Pcurve,inverse_den)

	# Prime field exponentiation: raise num to power mod p
	def field_exp(self,num,power):
		return pow(num%self.Pcurve,power,self.Pcurve)
	# Return the special identity point
	#   We pick x=p, y=0
	def identity(self):
		return ECpoint(self,self.Pcurve,0,1)

	# addition function point  
	def ECadd(a,b): # Not true addition, fist case x1 != x2 invented for EC. Could have been called anything.
	    #LamAdd , b[1] = y2 , a[1]= y1 
	    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) % Pcurve
	    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
	    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
	    return (x,y)
	#multiplication point 
	def ECdouble(a): # This is called point doubling, also invented for EC.
	    Lam = ((3*a[0]*a[0]+Acurve) * modinv((2*a[1]),Pcurve)) % Pcurve
	    x = (Lam*Lam-2*a[0]) % Pcurve
	    y = (Lam*(a[0]-x)-a[1]) % Pcurve
	    return (x,y)

