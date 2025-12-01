def main():
    all_ingredients = set()
    all_allergens = set()
    food_list = []

    with open("21-1_input.txt") as f:
        for index, line in enumerate(f):
            line = line.strip()
            food_list.append([])
            left = line.split("(")[0].strip()
            food_list[index].append([])
            for i in left.split(" "):
                all_ingredients.add(i)
                food_list[index][0].append(i)
            right = line.split("(")[1].strip(") ")
            food_list[index].append([])
            for i in right.split(" "):
                i = i.strip(",")
                if i != "contains":
                    all_allergens.add(i)
                    food_list[index][1].append(i)
                

    all_allergens = {i:list(all_ingredients) for i in all_allergens}
    for i in all_allergens:
        for j in food_list:
            if i in j[1]:
                temp = []
                for k in all_allergens[i]:
                    if k in j[0]:
                        temp.append(k)
                all_allergens[i] = list(temp)

    possibles = set()
    for i in all_allergens.values():
        for j in i:
            possibles.add(j)
            
    total = 0
    for i in food_list:
        for j in i[0]:
            if j not in possibles:
                total += 1
    print(total)


if __name__ == "__main__":
    main()



