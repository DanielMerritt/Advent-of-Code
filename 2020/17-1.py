import copy

def pad(lst):
    temp = list(lst)
    for index, i in enumerate(temp): #x padding
        for jindex, j in enumerate(temp[0]):
            temp[index][jindex] = ["."]+list(temp[index][jindex])+["."]
    temp2 = ["." for _ in range(len(temp[index][0]))]
    temp3 = []
    for index, i in enumerate(temp): #y padding
        temp3.append(list(temp2))
        for jindex, j in enumerate(temp[index]):
            temp3.append(list(temp[index][jindex]))
        temp3.append(list(temp2))
        temp[index] = list(temp3)
        temp3 = []
    temp2 = [["." for i in range(len(temp[0]))] for j in range(len(temp[0]))]
    temp3 = [] #z padding
    temp3.append(list(temp2))
    for index, i in enumerate(temp):
        temp3.append(list(temp[index]))
    temp3.append(list(temp2))
    temp = list(temp3)
    return temp

def get_combinations(coordinate):
    output = []
    for i in range(coordinate[0]-1,coordinate[0]+2):
        for j in range(coordinate[1]-1,coordinate[1]+2):
            for k in range(coordinate[2]-1,coordinate[2]+2):
                if (i,j,k) != coordinate:
                    output.append((i,j,k))
    return output
                    
        

def main():
    current = [[]]

    with open("17-1_input.txt") as f:
        for line in f:
            line = line.strip()
            temp = [i for i in line]
            current[0].append(temp)

    for _ in range(6):        
        for i in range(2):
            current = list(pad(current))
        temp = copy.deepcopy(current)
        for index, i in enumerate(current[1:-1],1):
            for jindex, j in enumerate(i[1:-1],1):
                for kindex, k in enumerate(j[1:-1],1):
                    combs = get_combinations((index,jindex,kindex))
                    count = 0
                    for l in combs:
                        if current[l[0]][l[1]][l[2]] == "#":
                            count += 1
                    if current[index][jindex][kindex] == "#" and not(2 <= count <= 3):
                        temp[index][jindex][kindex] = "."
                    if current[index][jindex][kindex] == "." and count == 3:
                        temp[index][jindex][kindex] = "#"
        current = copy.deepcopy(temp)      
                
    count = 0

    for i in current:
        for j in i:
            for k in j:
                if k =="#":
                    count += 1
    print(count)



if __name__ == "__main__":
    main()
                
        
