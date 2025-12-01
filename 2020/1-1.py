def main():
    with open("1-1_input.txt") as f:
        data = [int(i) for i in f]
        for i in data:
            for j in data:
                if i+j == 2020:
                    print(i*j)
                    return

if __name__ == "__main__":
    main()


        
