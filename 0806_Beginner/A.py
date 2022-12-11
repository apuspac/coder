def full_house(num_list):
    double = False
    triple = False

    for num in range(len(num_list)):
        num_c = num_list.count(num_list[num])
        if 2 == num_c:
            double = True
        if 3 == num_c:
            triple = True

    if double == True and triple == True:
        return "Yes"
    else:
        return "No"


def main():
    num_5 = input().split()
    # num_5 = [1, 2, 1, 2, 1]
    result = full_house(num_5)

    print(result)


main()
