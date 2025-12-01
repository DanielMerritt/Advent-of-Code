def main():
    with open("13-1_input.txt") as f:
        for index, line in enumerate(f):
            line = line.strip()
            if index == 0:
                earliest_depart = int(line)
            else:
                buses = line.split(",")
                buses = [int(j) for j in buses if j != "x"]

    waits = {i-earliest_depart%i:i for i in buses}
    print(min(waits.keys())*waits[min(waits.keys())])

if __name__ == "__main__":
    main()
