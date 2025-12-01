def main():
    puzzle_input = "327465189"
    seq = [i for i in puzzle_input]
    seq += [str(i) for i in range(10, 1000001)]
    dic = {i:seq[index+1] for index, i in enumerate(seq[:-1])}
    dic["1000000"] = puzzle_input[0]

    current = puzzle_input[0]
    for i in range(10000000):
        temp_dic = {}
        pick_up = []
        temp = current
        for i in range(3):
            temp = dic[temp]
            pick_up.append(temp)

        temp = int(current)
        while True:
            temp = temp - 1
            if temp < 1:
                temp = 1000000 - temp
            if str(temp) not in pick_up:
                break
            
        dest = str(temp)
        temp_dic[dest] = dic[current]
        temp_dic[pick_up[2]] = dic[dest]
        temp_dic[current] = dic[pick_up[2]]
        
        
        current = dic[pick_up[2]]
        for i in temp_dic:
            dic[i] = temp_dic[i]
            
    print(int(dic["1"])*int(dic[dic["1"]]))


if __name__ == "__main__":
    main()
