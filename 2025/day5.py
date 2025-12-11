def parse_input(filename: str) -> tuple[list[str], list[str]]:
    ranges: list[str] = []
    nums: list[str] = []
    current = "ranges"
    with open(filename) as f:
        for line in f:
            if not line.strip():
                current = "nums"
                continue
            if current == "ranges":
                ranges.append(line.strip())
            elif current == "nums":
                nums.append(line.strip())
    return ranges, nums


def part1(puzzle_input: tuple[list[str], list[str]]) -> int:
    total = 0
    for num in puzzle_input[1]:
        for current_range in puzzle_input[0]:
            lower_bound, upper_bound = map(int, current_range.split("-"))
            if lower_bound <= int(num) <= upper_bound:
                total += 1
                break
    return total


def part2(puzzle_input: tuple[list[str], list[str]]) -> int:
    intervals: list[tuple[int, int]] = []
    for id_range in puzzle_input[0]:
        lower_bound, upper_bound = map(int, id_range.split("-"))
        intervals.append((lower_bound, upper_bound))
    intervals.sort(key=lambda x: x[0])
    merged_ranges: list[list[int]] = []
    for start, end in intervals:
        if not merged_ranges:
            merged_ranges.append([start, end])
            continue
        _, previous_end = merged_ranges[-1]
        if start > previous_end + 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(previous_end, end)
    total = 0
    for start, end in merged_ranges:
        total += end - start + 1
    return total


def main() -> None:
    puzzle_input = parse_input("day5_input.txt")
    part1_result = part1(puzzle_input)
    part2_result = part2(puzzle_input)
    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")


if __name__ == "__main__":
    main()
