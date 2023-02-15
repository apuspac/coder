def main():
    leng, count = input().split()
    A = list(map(int, input().split()))

    for i in range(int(count)):
        del A[0]
        A.append(0)

    print(*A)


main()
