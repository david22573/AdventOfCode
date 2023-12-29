def extract_nums(line: str) -> tuple[tuple[int, int], int]:
    """Extracts source ranges and destination from a line of input."""
    nums = [int(num) for num in line.split()]
    destination, source, length = nums
    source_ranges = (source, source + length - 1)
    return source_ranges, destination


def map_seed(seed: int, ranges: list) -> int:
    """Maps a seed to its new location based on given ranges."""
    for source_ranges, destination in ranges:
        if source_ranges[0] <= seed <= source_ranges[1]:
            offset = seed - source_ranges[0]
            return destination + offset
    return seed  # No matching range, return the original seed


def extract_seeds(line: str) -> list[tuple[int, int]]:
    """Extracts seed pairs (starting seed, range) from the first line."""
    line = line.split(":")[1].strip()
    seeds = line.split()
    return [(int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)]


class Solution:
    def __init__(self, content: list[str]) -> None:
        self.content = content

    def part_one(self) -> int:
        """Calculates the minimum seed location for part one."""
        seeds = extract_seeds(self.content[0])
        seed_locations = []
        ranges = []

        for starting_seed, range_ in seeds:
            for seed in range(starting_seed, starting_seed + range_):
                for line in self.content[2:]:
                    if line == "" or line == self.content[-1]:
                        seed = map_seed(seed, ranges)
                        ranges = []
                    elif line[0].isdigit():
                        source_ranges, destination = extract_nums(line)
                        ranges.append((source_ranges, destination))
                seed_locations.append(seed)

        return min(seed_locations)

    def part_two(self) -> int:
        """Calculates the minimum seed location for part two."""
        seeds = extract_seeds(self.content[0])
        seed_locations = []

        for starting_seed, range_ in seeds:
            for seed in range(starting_seed, starting_seed + range_):
                for line in self.content[2:]:
                    if line == "" or line == self.content[-1]:
                        seed = map_seed(seed, ranges)
                        ranges = []
                    elif line[0].isdigit():
                        source_ranges, destination = extract_nums(line)
                        ranges.append((source_ranges, destination))
                seed_locations.append(seed)

        return min(seed_locations)

    def solve(self, part_two=False) -> int:
        """Solves the problem for the specified part."""
        return self.part_two() if part_two else self.part_one()

