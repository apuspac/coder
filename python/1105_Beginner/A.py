def main():
    str_a = input()

    result = str_a.rfind("a")
    if result != -1:
        result = result + 1

    print(result)


main()
