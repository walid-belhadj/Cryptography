def on_curve(a,b):
	return y**2==x**3+x+1725858433486651246286

def sum1(cur,p1,p2):
	"""compute p1+p2 on the elliptic curve cur"""
	lam = (p2[1]-p1[1])/(p2[0]-p1[0])
	nu = p1[1] - lam*p1[0]
	x3 = lam**2 - cur[0] - p1[0] - p2[0]
	y3 = -(lam * x3 + nu)
	return (x3,y3)
curve17=(0,0,17)
p1=(-1,4)
p2=(2,5)
elliptic.sum1(curve17,p1,p2)
(-1, -4)

def multi_2(cur,p,n):
	"""Multiply n*p on the elliptic curve cur (uses while)"""
	r=p
	while n>1:
		r=sum(cur,r,p)
		n-=1
	return r

def multi_1(cur,p,n):
	"""Multiply n*p on the elliptic curve cur"""
	r=p
	for k in range(0,n-1):
		r=sum(cur,r,p)
	return r

#find factors
def factor(n):
	d = 2
	factors= [ ]
	whilen > 1:
		if n % d == 0:
			factors.append(d)
			n = n/d
		else:
			d = d + 1
	return factors
#facotrial 
> def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)
#modulopower
def modpower(b,e,n):
	result= 1
	s = b
	q = e
	while q > 0:
		r = q % 2
		if r == 1:
			result= result*s% n
			# printq, r, s, result
		s = s*s % n
		q = q/2
	return result
def modinv(a,n): #Extended Euclidean Algorithm/'division' in elliptic curves
# a = 10^-1 mod n = 17
    a = a % n
    for x in range(1,n):
    	if ((a*x) % n == 1):
    		return x
    return 1
#bezout 
 def bezout(a, b):
    ''' Calcule (u, v, p) tels que a*u + b*v = p et p = pgcd(a, b) '''
    if a == 0 and b == 0:
    	return (0, 0, 0)
    if b == 0:
    	return (a/abs(a), 0, abs(a))
    (u, v, p) = bezout(b, a%b)
    return (v, (u - v*(a/b)), p)
#pgcd 
def cal_gcd(a, b) : 
    if (a == 0) : 
        return b      
    return cal_gcd(b % a, a)

def cal_power(x, y, m) : 
    if (y == 0) :  
      return 1                
    p = cal_power(x, y // 2, m) % m 
    p = (p * p) % m 
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m)

def mod_Inv(a, m) :  
    gcd = cal_gcd(a, m) 
    if (gcd != 1) : 
        print("Inverse doesn't exist") 
    else : 
      print("Modmultipinverse: ", cal_power(a, m - 2, m))
  #O(log m).