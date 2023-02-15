def main():
    s = input()
    t = input()

    find_t = s.find(t)

    if find_t != -1:
        print("Yes")
    else:
        print("No")


main()
