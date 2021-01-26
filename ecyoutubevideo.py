INF_POINT = None


class EllipticCurve:
	#initialisation 
	def __init__(self, a, b, p):
		self.a = a
		self.b = b
		self.p = p
		self.points = [] # contenir tous les points du curve
		self.define_points()


	def define_points(self): # la liste est vide on rajoute le point infini
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
			return INF_POINT #  si x1=x2 et y1=-y2 

		if self.equal_modp(x1, x2) and self.equal_modp(y1, y2): # si p = q 
			u = self.reduce_modp((3 * x1 * x1 + self.a) * self.inverse_modp(2 * y1))
		else:
			u = self.reduce_modp((y1 - y2) * self.inverse_modp(x1 - x2))

		v = self.reduce_modp(y1 - u * x1)
		x3 = self.reduce_modp(u * u - x1 - x2)
		y3 = self.reduce_modp(-u * x3 - v)
		return (x3, y3)
	def print_points(self):
		print(self.points)
	def number_points(self):
		return len(self.points)
"""
"""
	def discriminant(self): # si ce n'est pas zero le EC existe  
		D = -16 *(4 * self.a * self.a * self.a + 27 * self.b * self.b)
		return self.reduce_modp(D)
	# helper functions

	def reduce_modp(self, x): # x mod p 
		return x % self.p


	def equal_modp(self, x, y): # difference is divisible par p x = y mod p 
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
#print("associative=" + str(ec.test_associativity()))
ec.print_points()


		"""count = 0 

for a in range(p):
	for b in range(p):
		ec = EllipticCurve(a, b, p)
		if ec.discriminant() == 0:
			continue
		count += 1
		print("a=" + str(a) + "   b=" + str(b))
		print("discriminant=" + str(ec.discriminant()))
		print("number points=" + str(ec.number_points()))
		print("associative=" + str(ec.test_associativity()))
		ec.print_points()
		print("--------------------------")
print("The number of elliptic curves over F_" + str(p) + " is: " + str(count))
		"""
"""	def test_associativity(self):
			n = len(self.points)
			for i in range (n):
				for j in range(n):
					for k in range(n):
						P = self.addition(self.points[i], self.addition(self.points[j], self.points[k]))
						Q = self.addition(self.addition(self.points[i], self.points[j]), self.points[k])
						if P != Q:
							return False
			return True """
	
