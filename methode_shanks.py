import math
def shanks_method_ecc(curve, G, H, order):

    m = int(math.ceil(gmpy2.sqrt(order))) # la partie entiere 
    L = {}

    # Bbs
    for j in range(0, m):
      P_tmp = curve.mul(j, G)
      L[str(P_tmp)] = j

    mG = curve.mul(m, G)

    # Gsts
    for i in range(0, m):
      P_tmp = curve.mul(i, mG)
      if not P_tmp.isInf():
        P_tmp = ecc.Point(P_tmp.x, (-P_tmp.y) % curve.p)

      P = curve.add(H, P_tmp)

      index = str(P)

      if index in L:
        return (L[index] + i*m) % curve.p

    return None

# trouver l'equation : G^x = H (mod curve.p)
def pohlig_hellman(curve, G, H):
    N = curve.p-1
    factors = decompose_order(N)
    x = 0


    for i in range(len(factors)):
      ni = factors[i][0]**(factors[i][1])
      tmp = N//ni
      G_prime = curve.mul(tmp, G)
      H_prime = curve.mul(tmp, H)

      # solution de  H_prime = x_prime*G_prime
      x_prime = shanks_method_ecc(curve, G_prime, H_prime, ni)
      while x_prime == None:
        order *= 2
        x_prime = shanks_method_ecc(curve, G_prime, H_prime, ni)

      # theoreme des restes chinois to find  x_prime = x (mod ni)
      (gcd, x0, x1) = xgcd(ni, tmp)

      x += x_prime*x1*tmp

    return x % N

# (A, B, N)
curve = ecc.Curve(1, 6, 11)
G = ecc.Point(5 , 6)
K = 19
H = curve.mul(K, G)

x = pohlig_hellman(curve, G, H)
print(" private key is : x = %s" % x)