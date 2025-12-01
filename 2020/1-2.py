def main():
    with open("1-1_input.txt") as f:
        data = [int(i) for i in f]
        for i in data:
            for j in data:
                for k in data:
                    if i+j+k == 2020:
                        print(i*j*k)
                        return
        
if __name__ == "__main__":
    main()
