def main():
    numbers = []
    for i in [1,2,3,5,7]:
        with open("3-1_input.txt") as f:
            current_index = 0
            trees = 0
            skip = False
            if i == 2:
                i = 1
                skip = True
            for index, line in enumerate(f):
                if skip == True and index % 2 == 1:
                    continue
                line = line.strip()
                if line[current_index%31] == "#":
                    trees += 1
                current_index += i
            numbers.append(trees)
            
    k  = 1
    for i in numbers:
        k*=i

    print(k)

if __name__ == "__main__":
    main()
