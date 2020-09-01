"""
Largest product in a series
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

...
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586 ...

Find the thirteen adjacent digits in the 1000-digit number that have
the greatest product. What is the value of this product?
"""
import sys
n = int(input())
b = ''.join(sys.stdin.read().split())
max_largest = 0
for i in range(1001 - n):
    largest = 1
    for j in range(i,i+n):
        largest *= int(b[j])
    max_largest = max(max_largest, largest)
print(max_largest)

