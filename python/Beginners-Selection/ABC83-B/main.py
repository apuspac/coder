n, a, b = map(int, input().split())

sum = 0
for i in range(1,n+1):
    list_i = list(str(i))

    list_sum = 0
    for j in list_i:
        list_sum += int(j)

    # print(list_sum)
    if list_sum >= a and list_sum <= b:
        sum += i

print(sum)