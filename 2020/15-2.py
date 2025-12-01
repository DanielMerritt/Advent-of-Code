def main():
    INPUT = 6,4,12,1,20,0

    dic = {i:index for index, i in enumerate(INPUT,1)}

    last = (16,7)
    for i in range(len(dic), 30000000):
        if last[0] not in dic:
            dic[last[0]] = last[1]
            last = (0, last[1] + 1)
        else:
            temp = last
            last = (last[1]-dic[last[0]], last[1] + 1)
            dic[temp[0]] = temp[1]

    if temp[1] == 30000000:
        print(temp[0])
    else:
        print(0)


if __name__ == "__main__":
    main()
