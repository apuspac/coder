import itertools


def main():
    N, M = map(int, input().split())

    ok_list = []
    comb_list = [i for i in range(N)]
    # print(comb_list)

    for i in range(N):
        S = list(input())

        for tmp in range(M):
            if S[tmp] == "o":
                S[tmp] = 1
            else:
                S[tmp] = 0

        ok_list.append(S)

    # print(ok_list)

    ans = 0

    all = itertools.combinations(comb_list, 2)

    for x in all:
        # print(x)

        clear_flag = 1
        for i in range(M):
            # print(ok_list[x[0]][i], ok_list[x[1]][i])

            if ok_list[x[0]][i] == 0 and ok_list[x[1]][i] == 0:
                clear_flag = 0
                break

        if clear_flag == 1:
            ans = ans + 1

    print(ans)


main()


"""
5 5
ooooo
oooxx
xxooo
oxoxo
xxxxx



3 2
ox
xo
xx
"""
