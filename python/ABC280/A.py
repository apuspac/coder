def main():
    h, w = map(int, input().split())

    sh = 0

    for i in range(h):
        grid = list(input())
        sh = sh + grid.count("#")

    print(sh)


main()
