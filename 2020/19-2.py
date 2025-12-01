from pyformlang.cfg import Production, Variable, Terminal, CFG

def main():
    rules = {}
    messages = []
    variables = {}
    productions = {}

    with open("19-2_input.txt") as f:
        part = 0
        for line in f:
            line = line.strip()
            if line == "":
                part += 1
                continue
            if part == 0:
                rule = ""
                for i in line:
                    if i.isnumeric():
                        rule += i
                    else:
                        break
                rules[rule] = line.split(":")[1].strip().replace('"', "").replace(" ", ",")
            if part == 1:
                messages.append(line)

    for i in rules:
        variables["var_"+i] = Variable(i)

    ter_a = Terminal("a")
    ter_b = Terminal("b")
    terminals = {"ter_a":Terminal("a"), "ter_b":Terminal("b")}

    count = 0
    for i in rules:
        if rules[i] == "a" or rules[i] == "b":
            productions["p"+str(count)] = Production(variables["var_"+i], [terminals["ter_"+rules[i]]])
            count += 1
        elif "|" in rules[i]:
            temp = rules[i].split("|")[0].strip(", ").split(",")
            temp2 = rules[i].split("|")[1].strip(", ").split(",")
            dest = [variables["var_"+j] for j in temp]
            dest2 = [variables["var_"+j] for j in temp2]
            productions["p"+str(count)] = Production(variables["var_"+i], dest)
            count += 1
            productions["p"+str(count)] = Production(variables["var_"+i], dest2)
            count += 1
        else:
            dest = [variables["var_"+j] for j in rules[i].split(",")]
            productions["p"+str(count)] = Production(variables["var_"+i], dest)
            count += 1
    initial = variables["var_0"]
    variables = set([variables[i] for i in variables])
    productions = set([productions[i] for i in productions])
    terminals = set([terminals[i] for i in terminals])

    cfg = CFG(variables, terminals, initial, productions)
    print(sum(1 for i in messages if cfg.contains(i)))



if __name__ == "__main__":
    main()

        
        
