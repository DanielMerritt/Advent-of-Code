def main():
    INPUT = 6,4,12,1,20,0,16

    lst = [i for i in INPUT]

    for i in range(len(lst), 2020):
        last = lst[-1]
        if last not in lst[:-1]:
            lst.append(0)
        else:
            lst.append(i-(len(lst)-1-lst[-2::-1].index(last)))

    print(lst[-1])

if __name__ == "__main__":
    main()
