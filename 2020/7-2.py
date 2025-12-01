class Bag:
    def __init__(self, colour, child_bags=[]):
        self.colour = colour
        if child_bags == ["no other bag"]:
            self.child_bags = []
        else:
            self.child_bags = child_bags
 

    def sum_child_bags(self):
        total = 0
        for i in self.child_bags:         
            number = ""
            for j in i:
                if j.isnumeric():
                    number += j
                else:
                    total += int(number)
                    break
        return total


    def bag_count(self, bag_storage):
        stack = ["1 " + self.colour]
        leaves_list = find_leaves("7-1_input.txt")
        count = 0
        while len(stack) != 0:
            if stack[-1][2:] not in leaves_list:
                temp = stack.pop()
                for i in bag_storage[temp[2:]].child_bags:
                    stack += int(i[0]) * [i]
                count += bag_storage[temp[2:]].sum_child_bags()
            else:
                stack.pop()                 
        return count
                            


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
            child_bags = [i.rstrip(".s") for i in child_bags]
            bag_storage[bag] = Bag(bag, child_bags)


    print(bag_storage["shiny gold bag"].bag_count(bag_storage))


if __name__ == "__main__":
    main()
