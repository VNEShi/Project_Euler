"""
Sum square difference
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
"""
n = int(input())
sumsq, sqsum = 0, 0
for i in range(1, n+1):
    sumsq += i
    sqsum += i ** 2
print((sumsq ** 2) - sqsum)

"""
for 1 line
print(sum(i for i in range(1, 11)) ** 2 - sum(i ** 2 for i in range(1, 11)))
"""

