def main():
    with open("5-1_input.txt") as f:
        max_id = 0
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
            if high * 8 + col_high > max_id:
                max_id = high*8 +col_high
    print(max_id)

if __name__ == "__main__":
    main()
