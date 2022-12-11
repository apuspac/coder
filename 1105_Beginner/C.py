import itertools


def main2():
    num_permu = input()
    permtation_tmp = input().split()

    permtation_tmp = tuple([int(n) for n in permtation_tmp])

    # for i in permtation_tmp:


def main():
    num_permu = input()
    permtation_tmp = input().split()

    permtation_tmp = tuple([int(n) for n in permtation_tmp])

    # print(num_permu)
    # print(permtation_tmp)

    permu_default = []
    for i in range(int(num_permu)):
        permu_default.append(i + 1)

    permtation_list = []
    index_tmp = 0
    perm_index = 0

    for i in itertools.permutations(permu_default):
        permtation_list.append(i)

        if i == permtation_tmp:
            perm_index = index_tmp
            break

        index_tmp = index_tmp + 1

    # print(permtation_list)

    # これ書いたけどそもそもitertools.permutationが辞書順ぽい？
    # index_tmp = 0
    # perm_index = 0
    # for i in permtation_list:
    #     index_tmp = index_tmp + 1
    #     if i == permtation_tmp:
    #         perm_index = index_tmp
    #         break

    print(" ".join(str(j) for j in permtation_list[perm_index - 1]))


# mainはTLE
# main()

main2()
