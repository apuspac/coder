import math


def count_prime(N):
    prime_list = []
    num = N

    for prime in range(2, N + 1):
        while (num % prime) == 0:
            prime_list.append(prime)
            num = num // prime

    return prime_list


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    k = int(input())

    a = factorization(k)
    # a = count_prime(k)

    print(max(a)[0])


# def main():
#     k = int(input())

#     i = 1
#     res = 1

#     while True:
#         res = res * i

#         if (res % k) == 0:
#             print(i)
#             break

#         i = i + 1


# def main():
#     k = int(input())

#     # print(check_divisor(k))

#     i = 0
#     while True:
#         if (math.factorial(i) % k) == 0:
#             print(i)
#             break

#         i = i + 1

main()
