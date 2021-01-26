INF_POINT = None
class PointOfCurve():
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
        
        return result

    def init_curve(self, pCurve, aCurve, bCurve, x, y, order=None):
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
            assert is_on_curve(self), 'NOT include this point'
        else:
            assert False, 'ERROR : Inadequate initialize'          
    def __str__(self):
        return 'Point : ( ' + str(self.x) + ', ' + str(self.y) + ')'
#Addition function
    def add_curve_points(self, other):
        
        if self.is_infinity:
            return other
        elif other ==INF_POINT:
            return self
        
        x1 = self.x
        y1 = self.y
        x2 = other.x
        y2 = other.y
        
        aCurve = self.aCurve
        bCurve = self.bCurve
        pCurve = self.pCurve
        rCurve = self.rCurve
        
        if x1 == x2 and ((y1 + y2) % pCurve) == 0: #case 2 course x1 = x2 and y1 = -y2
            return PointOfCurve(pCurve, aCurve, bCurve, None, None, rCurve)
        elif x1 == x2: #case 3 
            inv = inverse_mod(2 * y1, pCurve)
            lam_numerator = (3 * x1 * x1 + aCurve) % pCurve
            neu_numerator = (-(x1 * x1 * x1) + aCurve * x1 + 2 * bCurve) % pCurve
        else:
            inv = inverse_mod(x2 - x1, pCurve)
            lam_numerator = (y2 - y1) % pCurve
            neu_numerator = (y1 * x2 - y2 * x1) % pCurve
        
        lam = (lam_numerator * inv) % pCurve
        neu = (neu_numerator * inv) % pCurve
        
        x3 = (lam * lam - x1 - x2) % pCurve
        y3 = (-lam * x3 - neu) % pCurve
        
        return PointOfCurve(pCurve, aCurve, bCurve, x3, y3, rCurve)

    def mul_curve_points(self, other):
        """
        Definition of '*' between a point and a scalar number.
        This method supported 'point * scalar'.
        """
        s = abs(other)
        
        pCurve = self.pCurve
        aCurve = self.aCurve
        bCurve = self.bCurve
        rCurve = self.rCurve
        
        if other == 0:
            return PointOfCurve(pCurve, aCurve, bCurve, None, None, rCurve)
        
        result = PointOfCurve(pCurve, aCurve, bCurve, None, None, rCurve)
        tmp = self
        while s != 0:
            if s % 2 == 1:
                result = result + tmp
            tmp = tmp + tmp
            s //= 2
        
        if other < 0:
            result = PointOfCurve(pCurve, aCurve, bCurve, result.x, -result.y, rCurve)
        
        return result
#Definition multipli point*scalar
    def __rmul__(self, other):
        return self + other

# nbr of pts in EC see hasse's theoram o(p)
def search_order(point):
    order = 0
    i = 1
    while order == 0:
        check_point = point
        if check_point== INF_POINT  :
            order = i
            break
        i += 1
    assert order > 0, 'ERROR : order  is not found'
    return order

def inverse_mod(number, pCurve):
    inv_element = -1
    for i in xrange(pCurve):
        if (number * i) % pCurve == 1:
            inv_element = i
            break
p = 11
a = 1 
b = 6

ec = init_curve(p, a, b)


print("a=" + str(a) + "   b=" + str(b))
print("discriminant=" + str(ec.discriminant()))
print("number points=" + str(ec.number_points()))
ec.print_points()
print("--------------------------")