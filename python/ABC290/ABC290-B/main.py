a, b = map(int, input().split())

marubatu = list(input())


tousen = []

count = 1

for i in marubatu:
    if i == "o":
        if count <= b:
            tousen.append("o")
        else:
            tousen.append("x")
        count += 1
    else:
        tousen.append("x")

print("".join(map(str, tousen)))