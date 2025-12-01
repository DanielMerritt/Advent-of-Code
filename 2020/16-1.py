def main():
    rules = {}
    tickets = []

    with open("16-1_input.txt") as f:
        part = 0
        skip = False
        for i in f:
            if skip:
                skip = False
                continue
            i = i.strip()
            if i != "":
                if part == 0:
                    rules[i.split(":")[0]] = [i.split(" ")[-3], i.split(" ")[-1]]
                elif part >= 1:
                    tickets.append(i.split(","))
            else:
                part += 1
                skip = True
                continue

    valid_numbers  = set()
    for i in rules:
        for j in rules[i]:
            for k in range(int(j.split("-")[0]),int(j.split("-")[1])+1):
                valid_numbers.add(k)

    invalid_total = 0
    for i in tickets[1:]:
        for j in i:
            if int(j) not in valid_numbers:
                invalid_total += int(j)

    print(invalid_total)


if __name__ == "__main__":
    main()
