def main():
    N = int(input())
    S = list(input())

    mark_found = False

    for tmp in range(N):
        if S[tmp] == '"':
            mark_found = not mark_found
            # print(mark_found)

        if mark_found == False and S[tmp] == ",":
            # print("replace")
            S[tmp] = "."

    print("".join(S))


main()
