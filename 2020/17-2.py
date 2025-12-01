import copy

def pad(lst):
    temp = copy.deepcopy(lst)
    for index, i in enumerate(temp): #x padding
        for jindex, j in enumerate(temp[0]):
            for kindex, k in enumerate(temp[0][0]):
                temp[index][jindex][kindex] = ["."]+copy.deepcopy(temp[index][jindex][kindex])+["."]
                
    for index, i in enumerate(temp): #y padding
        temp2 = ["." for _ in range(len(temp[0][0][0]))]
        temp3 = []
        for jindex, j in enumerate(temp[0]):
            temp3.append(copy.deepcopy(temp2))
            for kindex, k in enumerate(temp[index][jindex]):
                temp3.append(copy.deepcopy(temp[index][jindex][kindex]))
            temp3.append(copy.deepcopy(temp2))
            temp[index][jindex] = copy.deepcopy(temp3)
            temp3 = []

    for index, i in enumerate(temp):        
        temp2 = [["." for i in range(len(temp[0][0]))] for j in range(len(temp[0][0]))] #z padding
        temp3 = []
        temp3.append(copy.deepcopy(temp2))
        for jindex, j in enumerate(temp):
            temp3.append(copy.deepcopy(temp[index][jindex]))
        temp3.append(copy.deepcopy(temp2))
        temp[index] = copy.deepcopy(temp3)

    temp2 = [[["." for i in range(len(temp[0][0]))] for j in range(len(temp[0][0]))] for k in range(len(temp[0]))]
    temp3 = [] #w padding
    temp3.append(copy.deepcopy(temp2))
    for index, i in enumerate(temp):
        temp3.append(copy.deepcopy(temp[index]))
    temp3.append(copy.deepcopy(temp2))
    temp = copy.deepcopy(temp3)
    return temp

def get_combinations(coordinate):
    output = []
    for i in range(coordinate[0]-1,coordinate[0]+2):
        for j in range(coordinate[1]-1,coordinate[1]+2):
            for k in range(coordinate[2]-1,coordinate[2]+2):
                for l in range(coordinate[3]-1,coordinate[3]+2):
                    if (i,j,k,l) != coordinate:
                        output.append((i,j,k,l))
    return output
                    
        

def main():
    current = [[]]

    with open("17-1_input.txt") as f:
        for line in f:
            line = line.strip()
            temp = [i for i in line]
            current[0].append(temp)
    temp = []
    temp.append(copy.deepcopy(current))
    current = copy.deepcopy(temp)

    for _ in range(6):        
        for i in range(2):
            current = copy.deepcopy(pad(current))
        temp = copy.deepcopy(current)
        for index, i in enumerate(current[1:-1],1):
            for jindex, j in enumerate(i[1:-1],1):
                for kindex, k in enumerate(j[1:-1],1):
                    for lindex, l in enumerate(k[1:-1],1):
                        if (index,jindex,kindex,lindex) == (1,1,1,8):
                            debug = True
                        combs = get_combinations((index,jindex,kindex,lindex))
                        count = 0
                        for l in combs:
                            if current[l[0]][l[1]][l[2]][l[3]] == "#":
                                count += 1
                        if current[index][jindex][kindex][lindex] == "#" and not(2 <= count <= 3):
                            temp[index][jindex][kindex][lindex] = "."
                        if current[index][jindex][kindex][lindex] == "." and count == 3:
                            temp[index][jindex][kindex][lindex] = "#"
        current = copy.deepcopy(temp)

    count = 0

    for i in current:
        for j in i:
            for k in j:
                for l in k:
                    if l =="#":
                        count += 1
    print(count)


if __name__ == "__main__":
    main()
    
                
        
