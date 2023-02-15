from unittest import result


def nice_grid(grid):
    pass


def main():
    grid = input().split()
    grid = [int(i) for i in grid]
    result = nice_grid(grid)

    print(result)


main()
