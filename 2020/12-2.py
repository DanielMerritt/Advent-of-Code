def main():
    directions = {"N":0,"E":0,"S":0,"W":0}
    directions_lst = ["N","E","S","W"]
    current_waypoint = {"N":1,"E":10,"S":0,"W":0}

    with open("12-1_input.txt") as f:
        for i in f:
            i = i.strip()
            if i[0] == "F":
                for j in directions:
                    directions[j] += current_waypoint[j]*int(i[1:]) 

            elif i[0] == "R":
                temp = dict(current_waypoint)
                for j in current_waypoint:
                    temp[j] = current_waypoint[directions_lst[(directions_lst.index(j)\
                                                    - (int(i[1:])//90))%4]]
                current_waypoint = dict(temp)
            elif i[0] == "L":
                temp = dict(current_waypoint)
                for j in current_waypoint:
                    temp[j] = current_waypoint[directions_lst[(directions_lst.index(j)\
                                                    + (int(i[1:])//90))%4]]
                current_waypoint = dict(temp)
            else:
                current_waypoint[i[0]] += int(i[1:])

    print(abs(directions["N"]-directions["S"])+abs(directions["E"]-directions["W"]))


if __name__ == "__main__":
    main()
