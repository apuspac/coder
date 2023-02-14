def check_kaibun(word, count):
    for index in range(int(count / 2)):

        if word[index] != word[-index - 1]:
            # print("index: {0} {1} {2}".format(index, word[index], word[-index - 1]))
            return "No"
    return "Yes"


def word_replace(word, arrow):
    s_replace = "AB"
    okikae = word[:arrow] + s_replace + word[arrow + len(s_replace) :]
    # print(okikae)

    return okikae


def okikae(word, count):
    for index in range(int(count / 2)):

        if word[index] != word[-index - 1]:
            if word[index] == "A" and index != 0:
                word = word_replace(word=word, arrow=index - 1)
            elif word[index] == "B":
                word = word_replace(word=word, arrow=index)
                # print("index {0}, {1}".format(index, word))
        print("index {0}, {1}".format(index, word))

    return check_kaibun(word=word, count=count)


def main():
    # strで受け取る
    word_count = int(input())
    word = input()

    # 正解
    print("Yes" if (word[0] == "B" or word[-1] == "A") and word != "BA" else "No")

    # word = "AAABBBB"
    # word_count = len(word)

    result = okikae(word, word_count)

    # print("result: {0}".format(result))
    print(result)


main()
