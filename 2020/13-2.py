def main():
    with open("13-1_input.txt") as f:
        for index, line in enumerate(f):
            line = line.strip()
            if index == 0:
                continue
            else:
                buses = line.split(",")

    eqs = [[int(i)-index, int(i),1] for index, i in enumerate(buses) if i != "x"]
    for i in range(len(eqs)):
        for j in range(len(eqs)):
            if j != i:
                eqs[j][2] *= eqs[i][1]

    for index, i in enumerate(eqs):
        temp = i[2] % i[1]
        temp2 = list(i)
        while temp != i[0]%i[1]:
            eqs[index][2] += temp2[2]
            temp = eqs[index][2] % i[1]

    mod = 1
    for i in eqs:
        mod *= i[1]
    print(sum(i[2] for i in eqs)%mod)


if __name__ == "__main__":
    main()
