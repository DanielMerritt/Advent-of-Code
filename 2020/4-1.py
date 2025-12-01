def main():
    with open("4-1_input.txt") as f:
        current_stats = []
        valid_total = 0
        invalid = False
        needed_stats = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        for line in f:
            line = line.strip()
            if line == "":
                for j in needed_stats:
                    if j not in current_stats:                     
                        invalid = True
                        break
                if not invalid:
                    valid_total += 1
                invalid = False
                current_stats = []
                continue

            for i in line.split(" "):
                current_stats.append(i.split(":")[0])
        for j in needed_stats:
            if j not in current_stats:                     
                invalid = True
                break
            if not invalid:
                valid_total += 1
            invalid = False
            current_stats = []
             
    print(valid_total)

if __name__ == "__main__":
    main()
