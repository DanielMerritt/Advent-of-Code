def gen_combinations(address):
    lst = [bin(i)[2:] for i in range(2**address.count("X"))]
    lst = [(address.count("X")-len(i))*"0"+i for i in lst]
    combinations = []
    for i in range(len(lst)):
        temp = 0
        temp2 = address
        for j in range(len(address)):
            if address[j] == "X":
                temp2 = temp2[:j]+lst[i][temp]+temp2[j+1:]
                temp += 1
        combinations.append(int(temp2,2))
    return combinations
    
    
def main():
    with open("14-1_input.txt") as f:
        mem_dict = {}
        for line in f:
            line = line.strip()
            if line[:4] == "mask":
                mask = line.split(" ")[-1]
           
            else:
                mem_address = bin(int(line.split("[")[1].split("]")[0]))[2:]
                mem_address = (36-len(mem_address))*"0"+mem_address
                value = int(line.split(" ")[-1])
                new = ""
                for i, j in zip(mask, mem_address):
                    if i == "X":
                        new += "X"
                    elif i == "0":
                        new += j
                    elif i == "1":
                        new += "1"
                combinations = gen_combinations(new)
                for i in combinations:
                    mem_dict[i] = value
                
                
        print(sum(mem_dict[i] for i in mem_dict))


if __name__ == "__main__":
    main()            
