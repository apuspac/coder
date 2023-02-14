import math

K = int(input())
MAX_N = 2 * 10**6

ans = 0
for i in range(1, MAX_N):
    gcd_k = math.gcd(K, i)
    K //= gcd_k
    if K == 1:
        print(i)
        exit()
print(K)
