def main():
    p1_deck = []
    p2_deck = []

    with open("22-1_input.txt") as f:
        player = 1
        for index, line in enumerate(f):
            line = line.strip()
            if index == 0:
                continue
            if line.isnumeric():
                if player == 1:
                    p1_deck.append(int(line))
                elif player == 2:
                    p2_deck.append(int(line))
            else:
                player = 2
                continue

    while len(p1_deck) != 0 and len(p2_deck) != 0:
        temp1 = p1_deck.pop(0)
        temp2 = p2_deck.pop(0)
        if temp1 > temp2:
            p1_deck.append(temp1)
            p1_deck.append(temp2)
        else:
            p2_deck.append(temp2)
            p2_deck.append(temp1)

    winner = p1_deck if len(p1_deck) > 0 else p2_deck

    print(sum(i * index for index, i in enumerate(winner[::-1], 1)))
        

if __name__ == "__main__":
    main() 
        
        
