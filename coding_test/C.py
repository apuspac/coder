# 約数列挙
# 参考: https://qiita.com/drken/items/a14e9af0ca2d857dad23

import math

# sqrt(N) まで探索すればいいアプローチ
def check_divisor(N):
    # divisor_list = []
    divisor_num = 0

    i = 1
    while i * i <= N:
        if N % 1 == 0:
            # divisor_list.append(i)
            divisor_num = divisor_num + 1

            # 重複しないときは N/iも push
            if N / i != i:
                # divisor_list.append(N / i)
                divisor_num = divisor_num + 1

        i = i + 1

    # return divisor_list
    return divisor_num


def count_prime(N):
    prime_list = []
    num = N

    for prime in range(2, N + 1):
        while (num % prime) == 0:
            prime_list.append(prime)
            num = num // prime

    return prime_list


def main():
    N = int(input())
    num_list = list(map(int, input().split()))

    oddeven = ["even", "odd"]

    for i in num_list:
        print(oddeven[check_divisor(i) % 2])


main()
