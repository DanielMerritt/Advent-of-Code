def main():
    puzzle_input = "327465189"
    current = [i for i in puzzle_input]
    current_loc = 0

    for i in range(100):
        new_loc = current[(current_loc + 4) % 9]
        current_label = current[current_loc]
        x = 1
        temp1 = current[(current_loc + 1) % 9]
        temp2 = current[(current_loc + 2) % 9]
        temp3 = current[(current_loc + 3) % 9]
        
        while True:
            temp4 = int(current_label)-x
            if temp4 <= 0:
                temp4 = 9 + temp4    
            destination = str(temp4)
            if destination not in (temp1, temp2, temp3):
                break
            else:
                x += 1
        if current_loc+1 >= len(current):
            temp1 = current.pop(0)
        else:
            temp1 = current.pop(current_loc+1)
        if current_loc+1 >= len(current):
            temp2 = current.pop(0)
        else:
            temp2 = current.pop(current_loc+1)
        if current_loc+1 >= len(current):
            temp3 = current.pop(0)
        else:
            temp3 = current.pop(current_loc+1)
        current.insert(current.index(destination)+1, temp1)
        current.insert(current.index(destination)+2, temp2)
        current.insert(current.index(destination)+3, temp3)
        current_loc = current.index(new_loc)


    print("".join(current[current.index("1")+1:] + current[:current.index("1")]))


if __name__ == "__main__":
    main()
