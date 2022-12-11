def main():
    h, w = map(int, input().split())

    s_columns = [[] * i for i in range(w)]
    t_columns = [[] * i for i in range(w)]

    for i in range(h):
        tmp_list = list(input())
        # print(tmp_list)
        for j in range(w):
            # print(tmp_list[j])
            s_columns[j].append(tmp_list[j])

    for i in range(h):
        tmp_list = list(input())
        # print(tmp_list)
        for j in range(w):
            # print(tmp_list[j])
            t_columns[j].append(tmp_list[j])

    re_list = [[] * i for i in range(w + 1)]

    for tmp in s_columns:
        re_list[tmp.count("#")].append(tmp)

    # print(s_columns)
    # print(t_columns)
    # print(re_list)

    find_flag = False
    all_find_flag = False

    for t_str in t_columns:
        count = t_str.count("#")

        find_flag == False

        # 見つける処理
        for re_str in re_list[count]:
            # print(t_str, re_str)
            if t_str == re_str:
                re_list[count].remove(t_str)
                find_flag = True
                break

        # 見つかんないと抜ける
        if find_flag == False:
            all_find_flag = True
            break

    if all_find_flag == False:
        print("Yes")
    else:
        print("No")


main()
