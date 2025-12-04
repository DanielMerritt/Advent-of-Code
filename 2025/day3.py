def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f]


def part1(puzzle_input: list[str]) -> int:
    total = 0
    for bank in puzzle_input:
        max_battery = max(bank[:-1])
        max_battery_index = bank.index(max_battery)
        second_max_battery = max(bank[max_battery_index + 1 :])
        total += int(max_battery + second_max_battery)
    return total


def part2(puzzle_input: list[str]) -> int:
    total = 0
    for bank in puzzle_input:
        max_number = ""
        for idx in range(-11, 0):
            max_battery = max(bank[:idx])
            max_number += max_battery
            max_battery_index = bank.index(max_battery)
            bank = bank[max_battery_index + 1 :]
        max_number += max(bank)
        total += int(max_number)
    return total


def main() -> None:
    puzzle_input = parse_input("day3_input.txt")
    part1_result = part1(puzzle_input)
    part2_result = part2(puzzle_input)
    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")


if __name__ == "__main__":
    main()
