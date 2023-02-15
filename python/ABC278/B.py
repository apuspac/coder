def main():
    hour, minits = input().split()

    int_h = int(hour)
    int_m = int(minits)

    while True:
        h = [int(a) for a in str(int_h)]
        m = [int(a) for a in str(int_m)]

        if len(h) < 2:
            h.insert(0, 0)

        if len(m) < 2:
            m.insert(0, 0)

        tmp_h = h[1]
        tmp_m = m[0]

        h[1] = tmp_m
        m[0] = tmp_h

        if h[0] == 0:
            check_h = h[1]
        else:
            check_h = int(str(h[0]) + str(h[1]))

        if m[0] == 0:
            check_m = m[1]
        else:
            check_m = int(str(m[0]) + str(m[1]))

        if check_h < 24 and check_m < 60:
            print(int_h, int_m)
            break

        int_m = int_m + 1

        if int_m == 60:
            int_m = 0
            int_h = int_h + 1

            if int_h == 24:
                int_h = 0


main()
