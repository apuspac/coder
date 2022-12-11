def main():
    n = int(input())

    if n < 16:
        print("0" + format(n, "x").upper())
    else:
        print(format(n, "x").upper())


main()
