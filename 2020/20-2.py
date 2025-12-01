class Piece:
    def __init__(self, ID, tile):
        self.ID = ID
        self.tile = tile

    def get_edges(self):
        self.top_edge = self.tile[0]
        self.bottom_edge = self.tile[-1]
        self.left_edge = [i[0] for i in self.tile]
        self.right_edge = [i[-1] for i in self.tile]
        self.edges = [self.top_edge, self.left_edge, self.bottom_edge,\
                      self.right_edge]       

    def get_nearby_tiles(self, tiles):
        self.adjacent = []
        for i in tiles:
            for jindex, j in enumerate(self.edges):
                if tiles[i] == self:
                    continue
                if j in tiles[i].edges or list(reversed(j)) in tiles[i].edges:   
                    self.adjacent.append((tiles[i].ID, self.edges[jindex]))
                    continue

    def rotate_tile(self):
        self.tile = list(zip(*self.tile[::-1]))
        self.get_edges()

    def flip_tile(self):
        self.tile = [i[::-1] for i in self.tile]
        self.get_edges()


def main():
    tiles = {}

    with open("20-1_input.txt") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Tile"):
                current = line.split(" ")[1][:-1]
                tiles[current] = Piece(current, [])
                continue
            if line != "":
                tiles[current].tile.append([i for i in line])

    for i in tiles:
        tiles[i].get_edges()
    for i in tiles:
        tiles[i].get_nearby_tiles(tiles)

    tile_order = []

    corners = [tiles[i].ID for i in tiles if len(tiles[i].adjacent) == 2]
    tile_order.append([corners[2]])
    tile_order[0].append(tiles[tile_order[0][0]].adjacent[0][0])
    tile_order.append([tiles[tile_order[0][0]].adjacent[1][0]])
    end = False
    x = 1
    while not end:
        for index, i in enumerate(tiles[tile_order[x][0]].adjacent):
            done = False
            left_column = [k[0] for k in tile_order]
            if i[0] in left_column:
                current = tiles[tile_order[x][0]]
                temp = current.adjacent[index][1]
                temp2 = current.edges[(current.edges.index(temp)+2)%4]
                for j in tiles[tile_order[x][0]].adjacent:
                    if j[1] == temp2:
                        if j[0] in corners:
                            end = True
                        tile_order.append([j[0]])
                        done = True
                        break
                if done:
                    break
        x += 1
    end = False
    x = 1
    while not end:
        for index, i in enumerate(tiles[tile_order[0][x]].adjacent):
            done = False
            if i[0] in tile_order[0]:
                current = tiles[tile_order[0][x]]
                temp = current.adjacent[index][1]
                temp2 = current.edges[(current.edges.index(temp)+2)%4]
                for j in tiles[tile_order[0][x]].adjacent:
                    if j[1] == temp2:
                        if j[0] in corners:
                            end = True
                        tile_order[0].append(j[0])
                        done = True
                        break
                if done:
                    break
        x += 1

    for i in range(1,int(len(tiles)**0.5)):
        for jindex, j in enumerate(tiles[tile_order[i][0]].adjacent):
            left_column = [k[0] for k in tile_order]
            if j[0] not in left_column:
                 tile_order[i].append(j[0])


    for k in range(1,int(len(tiles)**0.5)):
        end = False
        x = 1
        while not end:
            for index, i in enumerate(tiles[tile_order[k][x]].adjacent):
                done = False
                if i[0] in tile_order[k]:
                    current = tiles[tile_order[k][x]]
                    temp = current.adjacent[index][1]
                    temp2 = current.edges[(current.edges.index(temp)+2)%4]
                    for j in tiles[tile_order[k][x]].adjacent:
                        if j[1] == temp2:
                            tile_order[k].append(j[0])
                            done = True
                            if len(tile_order[k]) == int(len(tiles)**0.5):
                                end = True
                            break
                    if done:
                        break
            x += 1
    sea = []
    temp = tiles[tile_order[0][0]]
    rotate = False
    added = False
    while True:
        if rotate:
            temp.flip_tile()
        for _ in range(4):
            temp2 = [i[1] for i in temp.adjacent]
            temp3 = [i[1] for i in tiles[tile_order[0][1]].adjacent]
            if (temp.bottom_edge not in temp2 and list(reversed(temp.bottom_edge))\
               not in temp2 and temp.left_edge not in temp2 and\
               list(reversed(temp.left_edge)) not in temp2) and\
               (temp.right_edge in temp3 or list(reversed(temp.right_edge)) in temp3):
                added = True
                break
            else:
                temp.rotate_tile()
        if added:
            break
        else:
            rotate = True
    sea.append([temp.tile])


    for i in range(1,int(len(tiles)**0.5)):
        temp = tiles[tile_order[0][i]]
        rotate = False
        added = False
        while True:
            if rotate:
                temp.flip_tile()
            for _ in range(4):
                if temp.left_edge == tiles[tile_order[0][i-1]].right_edge:
                    added = True
                    break
                else:
                    temp.rotate_tile()
            if added:
                break
            else:
                rotate = True
        sea[0].append(temp.tile)

    for j in range(1,int(len(tiles)**0.5)):
        for i in range(int(len(tiles)**0.5)):
            temp = tiles[tile_order[j][i]]
            rotate = False
            added = False
            while True:
                if rotate:
                    temp.flip_tile()
                for _ in range(4):
                    if temp.bottom_edge == tiles[tile_order[j-1][i]].top_edge:
                        added = True
                        break
                    else:
                        temp.rotate_tile()
                if added:
                    break
                else:
                    rotate = True
                    
            if len(sea) <= j:
                sea.append([temp.tile])
            else:
                sea[j].append(temp.tile)

    for index, i in enumerate(sea):
        for jindex, j in enumerate(i):
            for kindex, k in enumerate(j):
                sea[index][jindex][kindex] = sea[index][jindex][kindex][1:-1]
            sea[index][jindex].pop()
            sea[index][jindex].pop(0)
    new = []
    for index, i in enumerate(sea):
        for x in range(7,-1,-1):
            temp = [sea[index][j][x] for j in range(int(len(tiles)**0.5))]
            new.append([j for k in temp for j in k])

    temp = [[1,0],[2,1],[2,4],[1,5],[1,6],[2,7],[2,10],[1,11],[1,12],\
            [2,13],[2,16],[1,17],[0,18],[1,18],[1,19]]


    lst = []
    for y in range(2):
        done = False
        for _ in range(4):
            for i in range(len(new)-2):
                for j in range(len(new[0])-19):
                    if all(new[i+x[0]][j+x[1]] == "#" for x in temp):
                        lst.append([(i+x[0], j+x[1]) for x in temp])
                        done = True
            if done:
                break
            new = list(zip(*new[::-1]))
        if done:
            break
        new = [i[::-1] for i in new]    

    lst = [j for i in lst for j in i]
    count = 0
    for index, i in enumerate(new):
        for jindex, j in enumerate(i):
            if j == "#":
                if (index,jindex) not in lst:
                    count += 1
    print(count)


if __name__ == "__main__":
    main()
