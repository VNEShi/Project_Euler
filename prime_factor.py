"""
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = int(input())
res = []
while n != 1:
    sqrt_n = int(n ** 0.5)
    count = 0
    for i in range(2,sqrt_n + 1):
        count += 1
        if n % i == 0:
            n = n / i
            break
    res.append(int(n))
    if count == sqrt_n - 1:
        n = n / n
print(res[len(res)-1])
