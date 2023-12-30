def extract_nums(line: str):
    nums = [int(num) for num in line.split()]
    destination, source, length = nums
    source_ranges = (source, source + length - 1)
    return (source_ranges, destination)


def seed_in_range(seed: int, source_ranges: tuple):
    start_range, stop_range = source_ranges
    return start_range <= seed <= stop_range


def map_seed(seed: int, ranges: list):
    for r in ranges:
        source_ranges, destination = r
        if seed_in_range(seed, source_ranges):
            start_range, stop_range = source_ranges
            offset = seed - start_range
            return destination + offset
    return seed


def extract_seeds(line: str):
    line = line.split(":")[1].strip()
    return [int(num) for num in line.split()]



class Solution:
    def __init__(self, content: list[str]):
        self.content = content

    def get_min_location(self, seeds):
        seed_locations = []
        ranges = []
        for seed in seeds:
            current_seed = seed
            for line in self.content[2:]:
                if line == "" or line == self.content[-1]:
                    next_seed = map_seed(current_seed, ranges)
                    ranges = []
                    current_seed = next_seed
                elif line[0].isdigit():
                    nums = extract_nums(line)
                    ranges.append(nums)
            seed_locations.append(current_seed)
        return seed_locations



    def part_one(self):
        seeds = extract_seeds(self.content[0])
        seed_locations = self.get_min_location(seeds)
        return min(seed_locations)

    def part_two(self):
         

    def solve(self, part_two=False):
        if part_two:
            return self.part_two()
        else:
            return self.part_one()
