def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().split(",")


def solve(puzzle_input: list[str]) -> tuple[int, int]:
    part1_total = 0
    part2_total = 0
    for product_id_range in puzzle_input:
        start, end = map(int, product_id_range.split("-"))
        for id in range(start, end + 1):
            str_id = str(id)
            id_len = len(str_id)
            if (
                len(str_id) % 2 == 0
                and str_id[: (id_len // 2)] == str_id[(id_len // 2) :]
            ):
                part1_total += id
            for i in range(1, (id_len // 2) + 1):
                if id_len % i != 0:
                    continue
                repeating_num = str_id[:i]
                if repeating_num * (id_len // i) == str_id:
                    part2_total += id
                    break
    return part1_total, part2_total


def main() -> None:
    puzzle_input = parse_input("day2_input.txt")
    part1_result, part2_result = solve(puzzle_input)
    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")


if __name__ == "__main__":
    main()
