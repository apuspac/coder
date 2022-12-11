import math


def main():
    a, b = map(float, input().split())

    # bは1増やした時の経過時間
    g = 1
    count = 0

    min_clock = b * count + a / math.sqrt(g)

    while True:
        g = g + 1
        count = count + 1

        time = b * count + a / math.sqrt(g)

        # print(time)

        if min_clock < time:
            break
        else:
            min_clock = time

    print(min_clock)


main()
