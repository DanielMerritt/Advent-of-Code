class Piece:
    def __init__(self, ID, tile):
        self.ID = ID
        self.tile = tile

    def get_edges(self):
        self.top_edge = self.tile[0]
        self.bottom_edge = self.tile[-1]
        self.left_edge = [i[0] for i in self.tile]
        self.right_edge = [i[-1] for i in self.tile]
        self.edges = [self.top_edge, self.bottom_edge, self.left_edge,\
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



    corners = (int(tiles[i].ID) for i in tiles if len(tiles[i].adjacent) == 2)
    x = 1
    for i in corners:
        x *= i
    print(x)


if __name__ == "__main__":
    main()
