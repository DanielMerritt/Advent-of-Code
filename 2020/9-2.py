def main():
    PART1 = 1504371145

    with open("9-1_input.txt") as f:
        lst = []
        for i in f:
            lst.append(int(i.strip()))

    starting_index = -1
    solved = False

    while not solved:
        starting_index += 1
        temp = []
        for i in range(len(lst)-starting_index):
            temp.append(lst[i+starting_index])
            if sum(temp) == PART1:
                solved = True
                break

    print(max(temp)+min(temp))


if __name__ == "__main__":
    main()

    


            
            
