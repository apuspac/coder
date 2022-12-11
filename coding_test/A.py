def main():
    N = input()
    B1 = list(input())
    B2 = list(input())

    Ans = []

    for b1, b2 in zip(B1, B2):
        if b1 == b2:
            Ans.append("0")
        else:
            Ans.append("1")

    print("".join(map(str, Ans)))


main()
