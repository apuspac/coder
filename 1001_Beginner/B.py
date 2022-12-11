def main():
    seq_query = input().split()

    seq_query = [int(n) for n in seq_query]

    seq = []
    for i in range(seq_query[0]):
        n = input().split()
        n = [int(i) for i in n]
        seq.append(n)

    query = []
    for i in range(seq_query[1]):
        n = input().split()
        n = [int(i) for i in n]
        query.append(n)

    # print(seq_query, seq, query)

    for now_query in query:
        # print(now_query)
        print(seq[now_query[0] - 1][now_query[1]])


main()
