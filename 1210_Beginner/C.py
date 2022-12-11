def calc(S, N, M_len):
    now_count = N % sum(M_len)
    # print(now_count)

    now_playing = 0

    for i in range(S):
        now_playing += M_len[i]
        if now_count <= now_playing:
            print(i + 1, M_len[i] - (now_playing - now_count))
            break


def main():
    S, N = map(int, input().split())
    list_music_len = list(map(int, input().split()))
    calc(S, N, list_music_len)

    # test_case = [3, 600, [180, 240, 120]]
    # calc(test_case[0], test_case[1], test_case[2])


main()
