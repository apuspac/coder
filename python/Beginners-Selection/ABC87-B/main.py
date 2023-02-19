a500 = int(input())
b100 = int(input())
c50 = int(input())
x = int(input())

count = 0
for i in range (a500+1):
    for j in range (b100+1):
        for k in range(c50+1):
            if i*500 + j * 100 + k *50 == x:
                count += 1
print(count)