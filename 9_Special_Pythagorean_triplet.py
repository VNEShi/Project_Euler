"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

"""
try:
    for a in range(1, 333):
        for b in range(a+1, (1000-a)//2+1):
            for c in range(b+1, 1000-a-b+1):
                if c**2 > a**2 + b**2:
                    break
                if a**2 + b**2 == c**2 and a + b + c == 1000:
                    raise Exception()
except:
    print(a*b*c)
"""


try:
    for a in range(1,333):
        for b in range(a+1,(1000-a)//2+1):
            c = 1000-a-b
            if c**2 == a**2 + b**2:
                raise Exception()
except:
    print(a*b*c)


