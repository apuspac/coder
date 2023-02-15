import re


def main():
    test_num = int(input())

    case_list = []
    for i in range(test_num):
        n = input().split()
        n = [int(i) for i in n]
        str_num = n[0]
        one_num = n[1]

        s = input()
        case_list.append([str_num, one_num, s])

    # # 1がつながっている箇所を探す
    # print(case_list)
    # print(case_list[0][2])
    # a = re.findall(r"1+\?+1?", case_list[0][2])

    print("---result---")

    # 1の個数を見てみる作戦
    for i in range(test_num):
        # 1を全部置換する
        replace_1 = case_list[i][2].replace("?", "1")
        print(replace_1)

        # 対応する場所を探す
        exp = str(1) + "{" + str(case_list[i][1]) + "}"
        print(exp)

        b = re.findall(exp, replace_1)

        print(b)


main()
