from pointOfCurve import PointOfCurve, search_order
INF_POINT = None
class EllipticCurve:
	def __init__(self, a, b, p):
		self.a = a
		self.b = b
		self.p = p
		self.points = []
		self.define_points()
		
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
        
        return result

    
    def search_order(self):
	    order = 0
	    i = 1	
	    while order == 0 :
	        check_point = i * self.points
	        if check_point == 0:
	            order = i
	            break
	        i += 1
	    assert order > 0, 'ERROR : order  is not found'
	    return order"""
	def search_order(self):
	    order = 0
	    i = 1	
	    while order == 0 :
	        check_point = i * self.points
	        if check_point == 0:
	            order = i
	            break
	        i += 1
	    assert order > 0, 'ERROR : order  is not found'
	    return order
	def define_points(self):
		self.points.append(INF_POINT)
		for x in range(self.p):
			for y in range(self.p):
				if self.equal_modp(y * y, x * x * x + self.a * x + self.b):
					self.points.append((x,y))

	def addition(self, P1, P2):
		if P1 == INF_POINT:
			return P2
		if P2 == INF_POINT:
			return P1

		x1 = P1[0]
		y1 = P1[1]
		x2 = P2[0]
		y2 = P2[1]

		if self.equal_modp(x1, x2) and self.equal_modp(y1, -y2):
			return INF_POINT

		if self.equal_modp(x1, x2) and self.equal_modp(y1, y2):
			u = self.reduce_modp((3 * x1 * x1 + self.a) * self.inverse_modp(2 * y1))
		else:
			u = self.reduce_modp((y1 - y2) * self.inverse_modp(x1 - x2))

		v = self.reduce_modp(y1 - u * x1)
		x3 = self.reduce_modp(u * u - x1 - x2)
		y3 = self.reduce_modp(-u * x3 - v)
		return (x3, y3)

	def number_points(self):
		return len(self.points)


	def discriminant(self):
		D = -16 *(4 * self.a * self.a * self.a + 27 * self.b * self.b)
		return self.reduce_modp(D)


	def print_points(self):
		print(self.points)


	# helper functions

	def reduce_modp(self, x):
		return x % self.p


	def equal_modp(self, x, y):
		return self.reduce_modp(x - y) == 0


	def inverse_modp(self, x):
		for y in range(self.p):
			if self.equal_modp(x * y, 1):
				return y
		return None

p = 11
a = 1 
b = 6

ec = EllipticCurve(a, b, p)

print("a=" + str(a) + "   b=" + str(b))
print("discriminant=" + str(ec.discriminant()))
print("number points=" + str(ec.number_points()))
ec.print_points()
print("--------------------------")

# get all the points an length
#x= search_order(ec)
#print("Point 1 order=" + str(x))
