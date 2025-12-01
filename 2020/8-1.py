def main():
    dic = {}
    with open("8-1_input.txt") as f:
        for index, i in enumerate(f):
            i = i.strip()
            dic[index] = i

    visited = []
    acc = 0
    current_loc = 0

    while True:
        if current_loc in visited:
            print(acc)
            return
        visited.append(current_loc)
        if "nop" in dic[current_loc]:
            current_loc += 1
            continue
        elif "acc" in dic[current_loc]:
            acc += int(dic[current_loc].split()[1])
            current_loc += 1
            continue
        elif "jmp" in dic[current_loc]:
            current_loc += int(dic[current_loc].split()[1])
        
    
if __name__ == "__main__":
    main()
