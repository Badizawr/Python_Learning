

from math import acos, pi

n = int(input('Точность округдения числа ПИ -> '))

def ValueOfPi(pi,a):
    pi = round ( 2 * acos( 0.0 ), a )
    return (pi)

print (ValueOfPi(pi,n))