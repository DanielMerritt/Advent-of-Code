def parse_input(filename: str) -> list[list[str]]:
    with open(filename) as f:
        return [list(line.strip()) for line in f]


def get_number_of_nearby_rolls(grid: list[list[str]], coord: tuple[int, int]) -> int:
    total = 0
    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            if x == coord[0] and y == coord[1]:
                continue
            if x < 0 or y < 0:
                continue
            try:
                if grid[y][x] == "@":
                    total += 1
            except IndexError:
                continue
    return total


def part1(grid: list[list[str]]) -> int:
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "@":
                nearby_rolls = get_number_of_nearby_rolls(grid, (x, y))
                if nearby_rolls < 4:
                    total += 1
    return total


def part2(grid: list[list[str]]) -> int:
    total = 0
    new_rolls_removed = -1
    while new_rolls_removed != 0:
        new_rolls_removed = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "@":
                    nearby_rolls = get_number_of_nearby_rolls(grid, (x, y))
                    if nearby_rolls < 4:
                        total += 1
                        new_rolls_removed += 1
                        grid[y][x] = "."
    return total


def main() -> None:
    puzzle_input = parse_input("day4_input.txt")
    part1_result = part1(puzzle_input)
    part2_result = part2(puzzle_input)
    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")


if __name__ == "__main__":
    main()
