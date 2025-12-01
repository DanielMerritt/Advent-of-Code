def main():
    outlets = [0]
    with open("10-1_input.txt") as f:
        for i in f:
            outlets.append(int(i.strip()))

    outlets.sort()
    outlets.append(outlets[-1]+3)
    current_jolts = 0
    diffs = []

    for i in outlets:
        diffs.append(i-current_jolts)
        current_jolts = i

    print(diffs.count(1)*diffs.count(3))

if __name__ == "__main__":
    main()
