import math


def main():
    money, deposit_type = map(int, input().split())

    interest_rate = [0.1, 0.2, 0.5, 0.2]

    for i in range(1, 73):
        money = money + money * interest_rate[deposit_type]

        if i == 24 or i == 48 or i == 72:
            print(math.floor(money))


main()
