def main():
    with open("2-1_input.txt") as f:
        count = 0
        for line in f:
            temp = 0
            line = line.strip()
            letter = line.split(":")[0][-1]
            first = int(line.split("-")[0])
            second = int(line.split(" ")[0].split("-")[1])
            line = line.split(" ")[-1]
            if line[first-1] == letter:
                temp += 1
            if line[second-1] == letter:
                temp += 1
            if temp == 1:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
