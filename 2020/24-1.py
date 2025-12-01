def main():
    directions_list = []

    with open("24-1_input.txt") as f:
        skip = False
        for line in f:
            line = line.strip()
            temp = []
            for index, i in enumerate(line):
                if skip:
                    skip = False
                    continue
                if i == "e" or i == "w":
                    temp.append(i)
                else:
                    temp.append(i + line[index+1])
                    skip = True
            directions_list.append(temp)


    grid = [["w" for i in range(50)] for j in range(50)]

    reference_point = (25,25)

    for i in directions_list:
        current = list(reference_point)
        for j in i:
            if current[0] % 2 == 0:
                if j == "e":
                    current = [current[0], current[1] + 1]
                elif j == "w":
                    current = [current[0], current[1] - 1]
                elif j == "ne":
                    current = [current[0] - 1, current[1]]
                elif j == "nw":
                    current = [current[0] - 1, current[1] - 1]
                elif j == "se":
                    current = [current[0] + 1, current[1]]
                elif j == "sw":
                    current = [current[0] + 1, current[1] - 1]
            else:
                if j == "e":
                    current = [current[0], current[1] + 1]
                elif j == "w":
                    current = [current[0], current[1] - 1]
                elif j == "ne":
                    current = [current[0] - 1, current[1] + 1]
                elif j == "nw":
                    current = [current[0] - 1, current[1]]
                elif j == "se":
                    current = [current[0] + 1, current[1] + 1]
                elif j == "sw":
                    current = [current[0] + 1, current[1]]
                
        if grid[current[0]][current[1]] == "w":
            grid[current[0]][current[1]] = "b"
            
        else:
            grid[current[0]][current[1]] = "w"  

    print(sum(1 for i in grid for j in i if j == "b"))

        
    
if __name__ == "__main__":
    main()

    
