def main():
    with open("14-1_input.txt") as f:
        mem_dict = {}
        for line in f:
            line = line.strip()
            if line[:4] == "mask":
                mask = line.split(" ")[-1]
           
            else:
                mem_address = line.split("[")[1].split("]")[0]
                value = bin(int(line.split(" ")[-1]))[2:]
                value = (36-len(value))*"0"+value
                new = ""
                for i, j in zip(mask, value):
                    if i == "X":
                        new += j
                    else:
                        new += i
                mem_dict[mem_address] = int(new,2)
        print(sum(mem_dict[i] for i in mem_dict))
                    

if __name__ == "__main__":
    main()
