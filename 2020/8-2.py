def main():
    dic = {}
    with open("8-1_input.txt") as f:
        for index, i in enumerate(f):
            i = i.strip()
            dic[index] = i

    solved = False

    for i in dic:
        if "acc" in dic[i]:
            continue
        elif "jmp" in dic[i]:
            temp = dict(dic)
            temp[i] = "nop" + temp[i][3:]
        elif "nop" in dic[i]:
            temp = dict(dic)
            temp[i] = "jmp" + temp[i][3:]
            
        visited = []
        acc = 0
        current_loc = 0
        while True:
            if current_loc == len(dic):
                solved = True
                break
            if current_loc in visited:
                break
            if current_loc == len(dic):
                solved = True
            visited.append(current_loc)
            if "nop" in temp[current_loc]:
                current_loc += 1
                continue
            elif "acc" in temp[current_loc]:
                acc += int(dic[current_loc].split()[1])
                current_loc += 1
                continue
            elif "jmp" in temp[current_loc]:
                current_loc += int(temp[current_loc].split()[1])
        if solved:
            print(acc)
            return

if __name__ == "__main__":
    main()
        
    

