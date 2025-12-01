def main():
    with open("3-1_input.txt") as f:
        current_index = 0
        trees = 0
        for line in f:
            line = line.strip()
            if line[current_index%31] == "#":
                trees += 1
            current_index += 3
        print(trees)
            
if __name__ == "__main__":
    main()
