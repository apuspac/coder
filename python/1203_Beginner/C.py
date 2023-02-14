def main():
    s = list(input())
    t = list(input())

    for i in range(len(t)):
        if i > (len(s) - 1):
            print(i + 1)
            break
        elif s[i] != t[i]:
            print(i + 1)
            break


main()
