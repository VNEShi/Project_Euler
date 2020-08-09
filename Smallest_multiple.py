"""
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
n = int(input())
def nod(a,b):
    if b > a:
        b, a = a, b
    while a % b != 0:
        a, b = b, a % b
    return b

def nok(a,b):
    if b > a:
        a, b = b, a
    return abs(a*b)/nod(a,b)

b = 1

for i in range(1,n+1):
    b = nok(i,b)
print(int(b))
