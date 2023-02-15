def main():
    user_num, ope_num = input().split()

    user_num = int(user_num) + 1
    ope_num = int(ope_num)

    user_list = []

    for i in range(user_num):
        tmp = []
        for i in range(user_num):
            tmp.append(0)

        user_list.append(tmp)

    # print(user_list)

    for i in range(ope_num):
        ope, user_1, user_2 = input().split()
        ope = int(ope)
        user_1 = int(user_1)
        user_2 = int(user_2)

        if ope == 1:
            user_list[user_1][user_2] = 1
        elif ope == 2:
            user_list[user_1][user_2] = 0
        elif ope == 3:
            if user_list[user_1][user_2] == 1 and user_list[user_2][user_1] == 1:
                print("Yes")
            else:
                print("No")

        # print(user_list)

    # print(user_list)


def main_2():
    user_num, ope_num = input().split()

    user_num = int(user_num) + 1
    ope_num = int(ope_num)

    user_list = [[] for i in range(user_num + 1)]

    for i in range(ope_num):
        ope, user_1, user_2 = input().split()
        ope = int(ope)
        user_1 = int(user_1)
        user_2 = int(user_2)

        if ope == 1:
            if user_2 in user_list[user_1] == False:
                user_list[user_1].append(user_2)
            print(user_2 in user_list[user_1])
        elif ope == 2:
            if user_2 in user_list[user_1]:
                user_list[user_1].remove(user_2)
        elif ope == 3:
            if user_2 in user_list[user_1] and user_1 in user_list[user_2]:
                print("Yes")
            else:
                print("No")

        print(user_list)


main_2()
