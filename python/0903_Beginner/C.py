def index_A(n ,m, num_ren):
    max_index = num_ren.index(max(num_ren))
    sum_sum = 0
    
    for i in range(m):
        sum_sum = sum_sum + (i + 1) * num_ren[max_index - (m - i - 1)]
        print(num_ren[max_index - (m - i - 1)])

    result = sum_sum
    return result


    


def main():
    # n, m = input().split()
    # num_ren = input().split()

    n = 10
    m = 4
    num_ren = ["-3", "1", "-4", "1", "-5",  "9",  "-2", "6" ,"-5","3"]

    num_ren = [int(i) for i in num_ren] 

    

    result = index_A(n, m, num_ren)    
    print(result)    


main()
