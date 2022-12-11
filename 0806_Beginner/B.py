def Ancestor(hito, oya):
    return hito - 1


def main():
    hito = int(input())
    oya = input().split()

    oya = [int(n) for n in oya]

    result = Ancestor(hito, oya)

    print(result)


main()
