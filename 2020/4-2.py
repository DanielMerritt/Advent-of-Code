def validate(stats):
    needed_stats = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for j in needed_stats:
        if j not in stats.keys():                     
            invalid = True
            return False
    if int(stats["byr"]) > 2002 or int(stats["byr"]) < 1920:
        return False
    if int(stats["iyr"]) > 2020 or int(stats["iyr"]) < 2010:
        return False
    if int(stats["eyr"]) > 2030 or int(stats["eyr"]) < 2020:
        return False
    if stats["hgt"][-2:] == "cm":
        if int(stats["hgt"][:-2]) > 193 or int(stats["hgt"][:-2]) < 150:
            return False
    elif stats["hgt"][-2:] == "in":
        if int(stats["hgt"][:-2]) > 76 or int(stats["hgt"][:-2]) < 59:
            return False
    else:
        return False
    if stats["hcl"][0] != "#":
        return False
    for i in stats["hcl"][1:]:
        if i not in [str(j) for j in range(10)] + ["a","b","c","d","e","f"]:
            return False
    if stats["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if len(stats["pid"]) != 9:
        return False
    else:
        for i in stats["pid"]:
            if i not in [str(j) for j in range(10)]:
                return False
    return True
    
def main():
    with open("4-1_input.txt") as f:
        current_stats = {}
        valid_total = 0
        for line in f:
            line = line.strip()
            if line == "":
                if validate(current_stats):
                    valid_total += 1
                current_stats = {}
                continue

            for i in line.split(" "):
                current_stats[i.split(":")[0]] = i.split(":")[1]
        if validate(current_stats):
            valid_total += 1
             
            
    print(valid_total)

if __name__ == "__main__":
    main()

