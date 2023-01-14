'''
Largest palindrome product
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
n = int(input())
max_n, min_n = int('9'*n), int('9'*(n-1))
max_palindr = 0
for i in range(max_n,min_n,-1):
    for j in range(i,min_n,-1):
        palindr = str(i*j)
        if palindr == palindr[-1::-1]:
            if max_palindr < int(palindr):
                max_palindr = int(palindr)
print(max_palindr)