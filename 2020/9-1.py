def is_valid(num, lst):
    valid = False
    for index, i in enumerate(lst):
        for index2, j in enumerate(lst):
            if index == index2:
                continue
            if i + j == num:
                valid = True
    return valid

def main():
    PREAMBLE = 25
    with open("9-1_input.txt") as f:
        lst = []
        for i in f:
            i = i.strip()
            if len(lst) < PREAMBLE:
                lst.append(int(i))
            else:
                if is_valid(int(i), lst):
                    lst.pop(0)
                    lst.append(int(i))
                else:
                    print(i)
                    break

if __name__ == "__main__":
    main()
            
