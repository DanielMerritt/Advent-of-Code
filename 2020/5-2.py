def process_input():
    with open("5-1_input.txt") as f:
        taken_seats = []
        for line in f:
            line = line.strip()
            high = 127
            low = 0
            r = 127
            col_high = 7
            col_low = 0
            col_r = 7
            for i in line:
                if i == "F":
                    r = (r-1)//2
                    high = low + r
                elif i == "B":
                    r = (r-1)//2
                    low = high - r
                elif i == "R":
                    col_r = (col_r-1)//2
                    col_low = col_high - col_r
                elif i == "L":
                    col_r = (col_r-1)//2
                    col_high = col_low + col_r
            taken_seats.append([high, col_high])
    return taken_seats

def main():
    taken_seats = process_input()
    potential_ids = []
    for i in range(1,127):
        for j in range(8):
            if [i,j] not in taken_seats:
                potential_ids.append(i*8+j)
    for i in potential_ids:
        if i-1 not in potential_ids and i+1 not in potential_ids:
            print(i)
            return


if __name__ == "__main__":
    main()

        

