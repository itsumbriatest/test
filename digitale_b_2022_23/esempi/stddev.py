def media(a, b):
    return (a+b)/2

def varianza(a, b):
    m = media(a, b)
    xa = (a - m)**2
    xb = (b - m)**2
    var = (xa + xb)/2
    return var

import math
def stddev(a, b):
    var = varianza(a, b)
    var = math.sqrt(var)
    return var

n1 = float(input("n1 = "))
n2 = float(input("n2 = "))
m = media(n1, n2)
v = stddev(n1, n2)
print(m, v)
