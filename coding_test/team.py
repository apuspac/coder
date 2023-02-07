import calendar
import pprint


def check_divisor(N):
    divisor_list, divisor_list2 = [], []
    divisor_num = 0

    i = 1
    while i * i <= N:
        if N % i == 0:
            #
            divisor_list.append(i)
            divisor_num = divisor_num + 1

            # 重複しないときは N/iも push
            if i != N // i:
                divisor_list2.append(N // i)
                divisor_num = divisor_num + 1
        i = i + 1

    return divisor_list + divisor_list2[::-1]
    # return divisor_num


def kisuu_3jou(n):
    sum = 0
    for i in range(n):
        if i % 2 != 0:
            print(i)
            print(i**3)
            sum += i**3

    return sum


def siawase():
    count = 0
    for i in range(1, 9999999):
        str_i = str(i)
        sum = 0
        for tmp in str_i:
            sum += int(tmp)

        if i % sum == 0:
            count += 1

    print(count)


def baka_3():
    sum = 0

    for i in range(1, 3333):

        if i % 3 == 0:
            sum += i
            # print(i)
        elif len(str(i)) == 3:
            sum += i
            # print(i)
        else:
            str_i = str(i)
            for tmp in str_i:
                if tmp == "3":
                    sum += i
                    print(i)
                    break

    print(sum + 3333)


def nimotu():
    sum = 0

    track = 0
    for i in reversed(range(1, 801)):
        if track + i < 5000:
            track += i
            print(track, i)
        else:
            track = 0
            track += i
            sum += 1
            print("change", track, sum)

    print(sum)


def yuriusu():
    count = 0
    for i in range(2001, 2200):
        for j in range(1, 13):
            list_a = calendar.monthcalendar(i, j)

            for k in list_a:
                if k[5] == 13:
                    pprint.pprint(list_a)
                    count += 1
                    print(i, j)


# [[0, 1, 2, 3, 4, 5, 6],
#  [7, 8, 9, 10, 11, 12, 13],
#  [14, 15, 16, 17, 18, 19, 20],
#  [21, 22, 23, 24, 25, 26, 27],
#  [28, 29, 30, 31, 0, 0, 0]]


def main():
    yuriusu()
    # nimotu()
    # baka_3()

    # siawase()

    # print(kisuu_3jou(100))
    # yakusu = check_divisor(1591349760)
    # # yakusu = check_divisor(605)

    # print(yakusu)
    # sum = 0

    # for i in yakusu:
    #     if i >= 10000 and i <= 99999:
    #         sum += i

    # print(sum)


main()
