from pointOfCurve import PointOfCurve, search_order
from signature import SignatureGenerator
from verification import SignatureVerificator

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if i * i > n:
                break
            elif n % i == 0:
                return False
        return True
#the function return maximum prime order.
def search_base_point(pCurve, aCurve, bCurve):
    lam = -1
    neu = -1
    max_order = -1
    for x in range(pCurve):
        for y in range(pCurve):
            if (y * y) % pCurve == ((x ** 3) + (aCurve * x) + bCurve) % pCurve:
                point = PointOfCurve(pCurve, aCurve, bCurve, x, y)
                point.order = search_order(point)
                print 'NOT prime order..., Search Next Point'
                if is_prime(point.order):
                    if max_order < point.order:
                        print 'Prime order is found!'
                        print 'order : ', point.order
                        print 'x : ', x
                        print 'y : ', y
                        lam = x
                        neu = y
                        max_order = point.order
    
    assert lam > -1 and neu > -1 and max_order > -1, "ERROR : Search is Failed"
    return lam, neu


def calculate_cofactor(pCurve, aCurve, bCurve, order):
    z = 0
    for x in range(pCurve):
        for y in range(pCurve):
            if (y * y) % pCurve == ((x ** 3) + (aCurve * x) + bCurve) % pCurve:
                z += 1
    print z
    print 'cofactor: ', z / order

def main():
    #p = 11
    #a = 1
    #b = 6
    print("**************ECDSA Signature****************")
    print("Enter the  curve elements y^2=x^3+ a * x + b ")
    aCurve=int(input("enter the value of a; "))
    bCurve=int(input("enter the value of b; "))
    pCurve=int(input("enter the value of P (prime); "))

    m =raw_input("enter the message to signe: ")
    print(m)

    x, y = search_base_point(pCurve, aCurve, bCurve)
    
    point = PointOfCurve(pCurve, aCurve, bCurve, x, y)
    point.order = search_order(point)
    calculate_cofactor(pCurve,aCurve,bCurve,point.order)
    
    sg = SignatureGenerator(point, m)
    pk = sg.get_public_key()
    print 'Q :', pk
    
    r, s = sg.get_signature()
   
    sv = SignatureVerificator(point, m)
    sv.verify_message(r, s, pk)


if __name__ == '__main__':
    main()