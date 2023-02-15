def main():
    num = input().split()
    num = [int(i) for i in num]

    A = num[0]
    B = num[1]
    C = num[2]
    D = num[3]
    E = num[4]
    F = num[5]

    ABC = A * B * C
    DEF = D * E * F

    waru = ABC - DEF

    print(waru % 998244353)


main()
