def recurse_combat(d1, d2):
    game_history = []
    p1_deck = list(d1)
    p2_deck = list(d2)
    while len(p1_deck) != 0 and len(p2_deck) != 0:
        if (p1_deck, p2_deck) in game_history:
            return ("p1", p1_deck)
        game_history.append((list(p1_deck), list(p2_deck)))
        temp1 = p1_deck.pop(0)
        temp2 = p2_deck.pop(0) 
        if len(p1_deck) >= temp1 and len(p2_deck) >= temp2:   
            if recurse_combat(p1_deck[:temp1], p2_deck[:temp2])[0] == "p1":
                p1_deck.append(temp1)
                p1_deck.append(temp2)
                continue
            else:
                p2_deck.append(temp2)
                p2_deck.append(temp1)
                continue
  
        if temp1 > temp2:
            p1_deck.append(temp1)
            p1_deck.append(temp2)
        else:
            p2_deck.append(temp2)
            p2_deck.append(temp1)
    return ("p1", p1_deck) if len(p1_deck) > 0 else ("p2", p2_deck)


def main():
    p1_starting_deck = []
    p2_starting_deck = []

    with open("22-1_input.txt") as f:
        player = 1
        for index, line in enumerate(f):
            line = line.strip()
            if index == 0:
                continue
            if line.isnumeric():
                if player == 1:
                    p1_starting_deck.append(int(line))
                elif player == 2:
                    p2_starting_deck.append(int(line))
            else:
                player = 2
                continue

    winner = recurse_combat(p1_starting_deck,p2_starting_deck)[1]
    print(sum(i * index for index, i in enumerate(winner[::-1], 1)))

if __name__ == "__main__":
    main()
