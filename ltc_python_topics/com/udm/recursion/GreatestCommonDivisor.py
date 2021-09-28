"""
     Euclidean Algo
    gcd (48, 18)
    steps 1 = 48/18 = 2 remainder 12
    step 2 = 18/12 = 1 remainder 6
    step 3 = 12/6 = 2 remainder 0  ( 6 is the greatest common divisor)

    base condition
    gcd (a, 0) = a
    gcd(a,b) = gcd(b, a mod b)
    """
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'Number must be integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b

    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(48, -1.8))
