def extract_nums(line: str):
    print(line)
    return [int(num) for num in line]


def extract_categories(line: str):
    line1, line2 = line.split('-to-')
    line2 = line2.split()[0]
    return line1, line2


def extract_seeds(line: str):
    line = line.split(":")[1].strip()
    return [int(num) for num in line.split()]


class Solution:
    def __init__(self, content) -> None:
        self.content = content
        self.category_map = {}

    def find_lowest_location(self):
        pass

    def map_categories(self, categories, nums):
        # seed-to-soil map:
        # 50 98 2
        # 52 50 48
        source, destination = categories
        destination, source, length = nums
        length -= 1
        destination_range = f"{destination} {destination+length}"
        source_range = f"{source} {source+length}"
        if destination not in self.category_map:
            self.category_map[destination][destination_range] = source_range

    def part_one(self):
        seeds = extract_seeds(self.content[0])
        for line in self.content:
            if 'to' in line:
                print(line)
                categories = extract_categories(line)
                source, destination = categories
            elif line and line[0].isdigit():
                nums = extract_nums(line)
                self.map_categories(categories, extract_nums(nums))
            elif len(line) == 0:
                pass
        print(self.category_map)
        return "Part One 1"

    def part_two(self):
        pass

    def solve(self):
        part_one = self.part_one()
        # part_two = self.part_two()
        return part_one
        # return part_one, part_two
