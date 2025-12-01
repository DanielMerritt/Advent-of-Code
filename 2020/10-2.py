def main():
    outlets = [0]
    with open("10-1_input.txt") as f:
        for i in f:
            outlets.append(int(i.strip()))
            
    outlets.sort()
    outlets.append(outlets[-1]+3)
    current_jolts = 0
    replaceable = {0:False}
    for index, i in enumerate(outlets[1:-1],1):
        if outlets[index+1]-outlets[index] == 3 or outlets[index]-outlets[index-1] == 3:
            replaceable[i] = False
        else:
            replaceable[i] = True
    replaceable[outlets[-1]] = False

    count = 0
    triples = 0
    temp = 0
    for i in replaceable:
        if replaceable[i]:
            count += 1
            temp +=1
        else:
            temp = 0
        if temp == 3:
            triples += 1

    print(2**(count-triples*3)*7**triples)


if __name__ == "__main__":
    main()
