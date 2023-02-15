from operator import mul
from functools import reduce
import itertools


def cmb(n, r):
    """組み合わせ総数の列挙

    Args:
        n (_type_): _description_
        r (_type_): _description_

    Returns:
        _type_: _description_
    """
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def permu(l):

    max = int(l[0] + l[1] + l[2])

    for v in itertools.permutations(l, 3):
        tmp = int(v[0] + v[1] + v[2])
        # print(tmp)
        if max < tmp:
            max = tmp

    return max


def permu_sp(l):
    max1 = [3, 2, 1]
    tmp_list = []
    for i in l:
        if max1[0] < len(i):
            tmp_list.append(len(i))
            tmp_list.append(max1[0])
            tmp_list.append(max1[1])
            max1 = tmp_list

    for i in l:
        keta = len(l)
        if not (max1[0] == keta or max1[1] == keta or max1[2] == keta):
            l.pop(l.index(i))

    list_3 = list(itertools.permutations(l, 3))

    max_list = [int(v[0] + v[1] + v[2]) for v in list_3]
    max_list = sorted(max_list, reverse=True)
    return max_list[0]

    # for v in itertools.permutations(l, 3):
    #     tmp = int(v[0] + v[1] + v[2])
    #     # print(tmp)
    #     if max < tmp:
    #         max = tmp

    # return max


def max_3(l):
    origin = l
    l = [int(i) for i in l]
    max_list = []

    index_0 = l.index(max(l))
    max_0 = l.pop(index_0)

    index_1 = l.index(max(l))
    max_1 = l.pop(index_1)

    index_2 = l.index(max(l))
    max_2 = l.pop(index_2)


#     print(str(max_0) + str(max_1) + str(max_2))


def ketamax_3(l):
    origin = l

    l = [int(i[0]) for i in l]
    first_max = max(l)
    max_list = []

    for i in origin:
        if first_max == int(i[0]):
            max_list.append(i)

    print(max_list)


def ans(l):
    l = [int(i) for i in l]
    l = sorted(l, reverse=True)

    max_list = [l[0], l[1], l[2]]

    list_3 = list(itertools.permutations(max_list, 3))
    max_list = [(str(v[0]) + str(v[1]) + str(v[2])) for v in list_3]

    return max(max_list)


def main():
    # l = ["1", "23", "4", "5", "54"]
    n = input()
    l = input().split()

    max = ans(l)
    print(max)


main()
