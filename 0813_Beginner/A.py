def main():
    first = input().split()
    first = [int(i) for i in first]

    # num_5 = [1, 2, 1, 2, 1]
    atcoder = "atcoder"

    print(atcoder[first[0] - 1 : first[1]])


main()
