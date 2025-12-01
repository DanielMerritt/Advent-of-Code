import string


def main():
    with open("6-1_input.txt") as f:
        total = 0
        temp = [i for i in string.ascii_lowercase]
        for line in f:
            line = line.strip()
            if line == "":
                total += len(temp)
                temp = [i for i in string.ascii_lowercase]
            else:
                temp2 = tuple(temp)
                for i in temp2:
                    if i not in line:
                        temp.pop(temp.index(i))
        total += len(temp)
    print(total)


if __name__ == "__main__":
    main()
