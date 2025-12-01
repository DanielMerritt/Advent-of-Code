def main():
    with open("2-1_input.txt") as f:
        count = 0
        for i in f:
            temp = 0
            letter = i.split(":")[0][-1]
            letter_min = int(i.split("-")[0])
            letter_max = int(i.split(" ")[0].split("-")[1])
            code = i.split()[-1]
            for i in code:
                if i == letter:
                    temp += 1
            if temp >= letter_min and temp <= letter_max:
                count += 1
        print(count)
        return

if __name__ == "__main__":
    main()
