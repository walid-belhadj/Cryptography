from random import randint

def is_prime(num, test_count):
	if num == 1:
	  return False
	if test_count >= num:
	   test_count = num - 1
	for x in range(test_count):
	    val = randint(1, num - 1)
	    if pow(val, num-1, num) != 1:
	       return False
	    return True

def generate_big_prime(n):
	found_prime = False
	while not found_prime:
	  p = randint(2**(n-1), 2**n)
	     if is_prime(p, 20):
	        return p	
X= input("limit range: ")
print(x)
	# inverse modulo 
	def inverse_mod(number, pCurve):
		inv_element = -1
		for i in xrange(pCurve):
			if (number * i) % pCurve == 1:
				inv_element = i
				break

		return inv_element
	# nbr of pts in EC see hasse's theoram o(p)
	def search_order(point):
		order = 0
		i = 1
		while order == 0:
			check_point = i * point
			if check_point.is_infinity:
				order = i
				break
			i += 1

		assert order > 0, 'ERROR : order  is not found'
		return order

# point dans la courbe elliptic
    def is_on_curve(point):
        x = point.x
        y = point.y
        aCurve = point.aCurve
        bCurve = point.bCurve
        pCurve = point.pCurve
    
        if (y * y) % pCurve == ((x**3) + (aCurve*x) + bCurve) % pCurve:
            result = True
        else:
            result = False
    def __init__ (self, pCurve, aCurve, bCurve, x, y, order=None):
        self.pCurve = pCurve
        self.aCurve = aCurve
        self.bCurve = bCurve
        self.rCurve = order
        self.is_infinity = False
        
        if x is None and y is None:
            self.x = None
            self.y = None
            self.is_infinity = True
        elif x is not None and y is not None:
            self.x = x % pCurve
            self.y = y % pCurve
            assert is_on_curve(self), 'n est pas  sur la courbe'
        else:
            assert False, 'ERROR : Inadequate initialize'  
        
        return result 

    def __str__(self):
       return 'Point : ( ' + str(self.x) + ', ' + str(self.y) + ')' 
