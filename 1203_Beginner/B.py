def main():
    n = int(input())
    list_s = list(map(int, input().split()))

    list_ans = []

    list_ans.append(list_s[0])
    tmp = list_s[0]

    for i in range(1, n):
        a = list_s[i] - tmp
        list_ans.append(a)
        tmp = list_s[i]

    print(*list_ans)


main()
