n, m = map(int, input().split())
list_a = list(map(int, input().split()))

list_b = list(map(int, input().split()))

count = 0
for i in list_b :
    count += list_a[i-1]

print(count)