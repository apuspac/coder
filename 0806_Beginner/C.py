import inspect
import itertools


def Monotonically_Increasing(length, max_num):
    # n_list = []

    # for i in range():
    # for i in range(max_num):
    #     n_list.append([i + 1])

    # print(n_list)
    print(inspect.getsource(itertools))


def main():
    # length, max_num = input().split()
    length = 2
    max_num = 3
    Monotonically_Increasing(int(length), int(max_num))

    # print(result)


main()
