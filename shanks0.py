def baby_step_giant_step(curve, G, H, order):

    m = int(math.ceil(gmpy2.sqrt(order)))
    L = {}


    # Baby steps
    for j in range(0, m):
      P_tmp = curve.mul(j, G)
      L[str(P_tmp)] = j

    mG = curve.mul(m, G)

    # Giant steps
    for i in range(0, m):
      P_tmp = curve.mul(i, mG)
      if not P_tmp.isInf():
        P_tmp = ecc.Point(P_tmp.x, (-P_tmp.y) % curve.p)

      P = curve.add(H, P_tmp)

      index = str(P)