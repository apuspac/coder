import itertools

l = [1, 2, 3, 4, 5]

count = 0
for v in itertools.permutations(l):
    if v[1] + v[0] == 7 or v[2] == 1:
        count += 1
        print(v)

print(count)