import collections


def inv(n, q):
    """div on PN modulo a/b mod q as a * inv(b, q) mod q
    >>> assert n * inv(n, q) % q == 1
    """
    n*inv % q = 1 => n*inv = q*m + 1 => n*inv + q*-m = 1
    # => egcd(n, q) = (inv, -m, 1) => inv = egcd(n, q)[0] (mod q)
    return egcd(n, q)[0] % q
    #[ref] naive implementation
    #for i in range(q):
    #    if (n * i) % q == 1:
    #        return i
    #    pass
    #assert False, "unreached"
    #pass

