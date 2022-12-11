import re

def split_pin(n):
    """関数の説明
    Args:
        n (引数の型): 引数の説明

    Returns:
        返す型: 返す変数の説明
    """
    result = "No"
    pin_up = ["0","0","0","0","0","0","0"]

    # pin探す
    if n[6] == "1":
        pin_up[0] = "1"

    if n[3] == "1":
        pin_up[1] = "1"

    if n[1] == "1" or n[7] == "1":
        pin_up[2] = "1"

    if n[0] == "1" or n[4] == "1":
        pin_up[3] = "1"

    if n[2] == "1" or n[8] == "1":
        pin_up[4] = "1"

    if n[5] == "1":
        pin_up[5] = "1"

    if n[9] == "1":
        pin_up[6] = "1"

    # print(pin_up)

    str_pin = "".join(pin_up)

    # print(re.search(r'1[01]*0[01]*1', str_pin))

    if re.search(r'1[01]*0[01]*1', str_pin):
        result = "Yes"

    return result


def main():
    n = input()

    if n[0] == "1":
        result = "No"
    else :
        result = split_pin(n)


    print(result)


main()
