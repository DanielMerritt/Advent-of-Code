class Bag:
    def __init__(self, colour, child_bags=[]):
        self.colour = colour
        if child_bags == ["no other bag"]:
            self.child_bags = []
        else:
            self.child_bags = child_bags
        
    def allowed_bags(self, bag_storage):
        leaves_list = find_leaves("7-1_input.txt")
        allowed_bags = tuple([self.colour]+self.child_bags)
        while True:
            temp = list(allowed_bags)
            for i in allowed_bags:
                if i not in leaves_list:
                    for j in bag_storage[i].child_bags:
                        if j not in temp:
                            temp.append(j)
            if len(allowed_bags) == len(temp):
                break
            allowed_bags = tuple(temp)
        return allowed_bags


def find_leaves(file):
    with open(file) as f:
        leaves_list = []
        for line in f:
            if "no other bags" in line:
                line = line.strip()
                leaves_list.append(line.split("contain")[0][:-2])
        return leaves_list


def main():                            
    bag_storage = {}

    with open("7-1_input.txt") as f:
        for line in f:
            line = line.strip()
            bag = line.split("contain")[0][:-2]
            child_bags = line.split("contain ")[1].split(", ")
            child_bags = [i.lstrip("0123456789 ") for i in child_bags]
            child_bags = [i.rstrip(".s") for i in child_bags]
            bag_storage[bag] = Bag(bag, child_bags)


    with open("7-1_input.txt") as f:
        count = 0
        for line in f:
            line = line.strip()
            bag = line.split("contain")[0][:-2]
            if "shiny gold bag" in bag_storage[bag].allowed_bags(bag_storage):
                count += 1
        print(count-1) # subtracting one since a gold bag needs to be in at least
                       # one other bag
            

if __name__ == "__main__":
    main()
