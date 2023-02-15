def main():
    book_num = int(input())
    vol = input().split()
    vol = [int(i) for i in vol]

    # print(book_num, vol)

    vol.sort()
    print(vol)

    can_read = []
    remain_book = vol

    for i in range(book_num):
        i = i + 1
        if remain_book[0] == i:
            can_read.append(i)
            remain_book.pop(0)
        else:
            if len(remain_book) > 1:
                del remain_book[-2:]
                can_read.append(i)
            else:
                break

    if len(can_read) == 0:
        print(0)
    else:
        print(can_read[-1])


main()
