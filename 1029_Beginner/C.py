import math


def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]


def main():
    sharp_list = []
    for i in range(9):
        n = list(input())

        # print(n)
        sharp = my_index_multi(n, "#")

        # print(sharp)

        for tmp in sharp:
            sharp_list.append((i + 1, tmp + 1))

    print(kyori(sharp_list[0], sharp_list[2]))

    distance = []

    for i in range(9):
        distance.append([])

        for j in range(len(sharp_list)):
            if i != j:
                distance[i].append(kyori(sharp_list[i], sharp_list[j]))

        print(distance[i])

    # print(distance)


# kyori(sharp_list[i], sharp_list[j])
# 二点間の距離
def kyori(x1, x2):
    return math.sqrt(pow((x2[0] - x1[0]), 2) + pow((x2[1] - x1[1]), 2))


main()
