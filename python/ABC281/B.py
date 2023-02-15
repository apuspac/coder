import random, string


def random_name(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return "".join(randlst)


def random_num(up, down):
    return random.randint(up, down)


def testcase():
    S = []
    for i in range(10):
        S.append(random_name(1) + str(random_num(0, 9999999)) + random_name(1))
    return S


def sample():
    sample = []
    sample.append("Q142857Z")
    sample.append("AB912278C")
    sample.append("X900000")
    sample.append("K012345K")
    sample.append("H2229612")
    return sample


def check(S):
    flag = 0
    flag_num = 0

    if len(S) != 8:
        flag = 1
        # print("len No")
    elif S[0].isalpha() == False or S[7].isalpha() == False:
        flag = 1
        # print("alpha No")
    elif S[0].isupper() == False or S[7].isupper() == False:
        flag = 1
        # print("upper No")
    else:
        num_s = ""
        for num in S[1:7]:
            if num.isdecimal() == False:
                flag_num = 1
                flag = 1
                break
            num_s += num

        if flag_num == 0:
            num_s = int(num_s)
            # print(num_s)

            if (num_s >= 100000 and num_s <= 999999) == False:
                flag = 1

    if flag == 0:
        print("Yes")
    else:
        print("No")


def main():
    # sample_case = sample()
    # test_case = testcase()

    # for i in sample_case:
    #     print(i)
    #     check(i)

    # for i in test_case:
    #     print(i)
    #     check(i)

    S = list(input())
    check(S)


main()
