def main():
    with open("6-1_input.txt") as f:
        total = 0
        temp = set()
        for line in f:
            line = line.strip()
            if line == "":
                total += len(temp)
                temp = set()
            else:
                for i in line:
                    temp.add(i)
        total += len(temp)
    print(total)

if __name__ == "__main__":
    main()
