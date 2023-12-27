def extract_nums(line: str):
    nums = [int(num) for num in line.split()]
    source, destination, length = nums
    source_ranges = (source, source + length - 1)
    return (source_ranges, destination)


def seed_in_range(seed: int, source_ranges: tuple):
    start_range, stop_range = source_ranges
    return seed >= start_range and seed <= stop_range


def map_seed(seed: int, ranges: list):
    mapped_seed = 0
    for r in ranges:
        source_ranges, destination = r
        start_range, stop_range = source_ranges
        if seed >= start_range and seed <= stop_range:
            offset = seed - start_range
            mapped_seed = destination + offset
        else:
            mapped_seed = seed

    return mapped_seed


def extract_seeds(line: str):
    line = line.split(":")[1].strip()
    return [int(num) for num in line.split()]


class Solution:
    def __init__(self, content: list[str]):
        self.content = content

    def part_one(self):
        seeds = extract_seeds(self.content[0])
        test_seed = seeds[0]
        ranges = []

        for line in self.content[1:]:
            if line != "" and line[0].isdigit():
                nums = extract_nums(line)
                ranges.append(nums)
            elif line == "":
                map_seed(test_seed, ranges)
                print(map_seed)
                ranges = []

        return 0

    def part_two(self):
        pass
