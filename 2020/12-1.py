def main():
    directions = {"N":0,"E":0,"S":0,"W":0}
    directions_lst = ["N","E","S","W"]
    current_direction = "E"

    with open("12-1_input.txt") as f:
        for i in f:
            i = i.strip()
            if i[0] == "F":
                directions[current_direction] += int(i[1:])

            elif i[0] == "R":
                current_direction = directions_lst[(directions_lst.index(current_direction)\
                                                    + (int(i[1:])//90))%4]
            elif i[0] == "L":
                current_direction = directions_lst[(directions_lst.index(current_direction)\
                                                    - (int(i[1:])//90))%4]
            else:
                directions[i[0]] += int(i[1:])

    print(abs(directions["N"]-directions["S"])+abs(directions["E"]-directions["W"]))

if __name__ == "__main__":
    main()
