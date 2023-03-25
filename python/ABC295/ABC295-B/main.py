r, c = map(int, input().split())

b_list = []
bom_list = []
ans_list = []
for i in range(r):
    b_n = list(input())
    b_list.append(b_n)

    for idx, boom in enumerate(b_n):
        if boom.isdigit() == True:
            bom_list.append([i, idx])

ans_list = b_list.copy()

def manhatan(x1, y1, x2, y2):
    return (abs(x1-x2) + abs(y2-y1))

ans_xy = []

for bom_xy in bom_list:
    bom_power = b_list[bom_xy[0]][bom_xy[1]]
    bom_power = int(bom_power)

    # print(bom_power)

    for i in range(r):
        for j in range(c):
            if manhatan(bom_xy[0], bom_xy[1], i, j) <= bom_power:
                ans_xy.append([i, j])

for c in ans_xy:
    ans_list[c[0]][c[1]] = "."


for i in b_list:
    print("".join(map(str,i)))