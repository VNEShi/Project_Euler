"""
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
n = int(input())
a = 0
for i in range(0,n,3):
    a += i
for i in range(0,n,5):
    if i % 15 != 0:
        a += i
print(a)
