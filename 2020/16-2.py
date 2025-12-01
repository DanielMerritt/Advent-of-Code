def main():
    rules = {}
    tickets = []

    with open("16-1_input.txt") as f:
        part = 0
        skip = False
        for i in f:
            if skip:
                skip = False
                continue
            i = i.strip()
            if i != "":
                if part == 0:
                    rules[i.split(":")[0]] = [i.split(" ")[-3], i.split(" ")[-1]]
                elif part >= 1:
                    tickets.append(i.split(","))
            else:
                part += 1
                skip = True
                continue
    valid_numbers  = set()
    for i in rules:
        for j in rules[i]:
            for k in range(int(j.split("-")[0]),int(j.split("-")[1])+1):
                valid_numbers.add(k)

    for i in tickets[1:]:
        for j in i:
            if int(j) not in valid_numbers:
                tickets.pop(tickets.index(i))
                break
            
    tickets_per_row = []
    for i in range(len(tickets[0])):
        temp = set()
        for j in tickets:
            temp.add(j[i])
        tickets_per_row.append(set(temp))

    possible_per_row = []
    for i in tickets_per_row:
        temp = set()
        for j in rules:
            temp2 = set()
            for k in rules[j]:
                for l in range(int(k.split("-")[0]),int(k.split("-")[1])+1):
                    temp2.add(l)
            if all(int(m) in temp2 for m in i):
                temp.add(j)
        possible_per_row.append(list(temp))
    rule_order = {}
    while len(rule_order) < len(rules):
        for index, i  in enumerate(possible_per_row):
            if len(i) == 1:
                rule_order[index] = i[0]
                temp = i[0]
                for jindex, j in enumerate(possible_per_row):
                    if temp in j:
                        possible_per_row[jindex].pop(j.index(temp))

    departures = [i for i in rule_order if rule_order[i].startswith("departure")]

    my_departures = [i for index, i in enumerate(tickets[0]) if index in departures]

    x = 1
    for i in my_departures:
        x *= int(i)

    print(x)



if __name__ == "__main__":
    main()



        
    
