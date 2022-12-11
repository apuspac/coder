def main():
    town, load = input().split()
    town = int(town)
    load = int(load)

    connect_town = [[] for i in range(town + 1)]

    for i in range(load):
        toshi_1, toshi_2 = input().split()
        toshi_1 = int(toshi_1)
        toshi_2 = int(toshi_2)

        connect_town[toshi_1].append(toshi_2)
        connect_town[toshi_2].append(toshi_1)

    connect_town = [sorted(i) for i in connect_town]

    for i in range(town):
        i = i + 1

        connect_town[i].insert(0, len(connect_town[i]))

        connect_town[i] = [str(i) for i in connect_town[i]]
        print(" ".join(connect_town[i]))


main()
