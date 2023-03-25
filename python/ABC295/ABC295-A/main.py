n = int(input())
w = input().split()

ans = False
for s in w:
    if s == "you" or s == "not" or s == "that" or s == "the" or s == "and":
       ans = True


if ans == True:
    print("Yes")
else :
    print("No")