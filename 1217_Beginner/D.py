import itertools

# 二部グラフ判定
def is_bipartite(colors, uv):
    # 記録用 点0の色を1(黒) とする。
    stack = [(0, 1)]

    while stack:
        vertex, color = stack.pop()
        # 着色
        colors[vertex] = color

        # 今の頂点から行けるところをチェック
        for extend_point in uv[vertex]:
            # 同じ色が隣接したらFalse
            if colors[extend_point] == color:
                return False

            # 未着色の場合は、反転してスタックに積む
            if colors[extend_point] == 0:
                stack.append((extend_point, -color))

    return True


def main():
    N, M = map(int, input().split())

    uv = [[] * i for i in range(N)]
    comb_list = [i for i in range(N)]
    all = list(itertools.combinations(comb_list, 2))

    for i in range(M):
        u, v = map(int, input().split())

        uv[v - 1].append(u - 1)
        uv[u - 1].append(v - 1)
        # uv.append(list(map(lambda i: i - 1, tmp)))

    print(uv)

    colors = [0 for i in range(N)]


main()
