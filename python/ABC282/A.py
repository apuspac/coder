def main():
    K = int(input())
    ans = []

    for i in range(65, 91 - (26 - K)):
        ans.append(chr(i))

    print("".join(ans))


main()
