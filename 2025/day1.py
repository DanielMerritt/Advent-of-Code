def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f]


def solve(puzzle_input: list[str]) -> tuple[int, int]:
    part1_total = 0
    part2_total = 0
    current_number = 50
    for line in puzzle_input:
        direction = line[0]
        value = int(line[1:])
        if direction == "L":
            if current_number == 0:
                num_rotations = value // 100
            else:
                num_rotations = ((100 - current_number) + value) // 100
            current_number = (current_number - value) % 100
            part2_total += num_rotations
        elif direction == "R":
            num_rotations, current_number = divmod(current_number + value, 100)
            part2_total += num_rotations
        else:
            raise ValueError("Invalid Direction")
        if current_number == 0:
            part1_total += 1
    return part1_total, part2_total


def main() -> None:
    puzzle_input = parse_input("day1_input.txt")
    part1_result, part2_result = solve(puzzle_input)
    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")


if __name__ == "__main__":
    main()
