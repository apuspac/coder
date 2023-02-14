import itertools


def calc(N, K, D, list_a):
    all = itertools.combinations(list_a, K)

    product = []
    for x in all:
        product.append(sum(x))

    # print(list(set(product)))

    product.sort()
    flag = 0
    for i in reversed(product):
        if i % D == 0:
            print(i)
            flag = 1
            break

    if flag == 0:
        print(-1)


def main():
    N, K, D = map(int, input().split())
    list_a = list(map(int, input().split()))
    calc(N, K, D, list_a)


main()
