"""
Large sum
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""
import sys
sums = 0
b = sys.stdin.read().split()
for nums in b:
    sums += int(nums)
print(int(str(sums)[0:10]))