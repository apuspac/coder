```
import sys
import pprint




def main(lines):    
    # load
    name_list = [[]]
    N = lines[0]

    for i, v in enumerate(lines):
        name_list.append(list(map(int, v.split())))
    
    name_list.pop(0)
    name_list.pop(0)

    count = 0

    while len(name_list) > 1:
        reverse_name = name_list.pop(0)[::1]
        reverse_name.reverse()
        
        for i in range(1, len(name_list)):
            if reverse_name == name_list[i]:
                # print(reverse_name, name_list[i], i)
                pop_j = name_list.pop(i)

                # print(pop_j)
                count += 1
                break
         
    print(count)




if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))

```