def read_input(path: str) -> list:
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]


def create_map(content: list) -> dict:
    seed_map = {}
    current_categories = []
    categories = set()
    for line in content:
        if line.find('-') != -1:
            line_categories = line.split(' ')[0].split('-to-')
            for category in line_categories:
                categories.add(category)
                if category not in seed_map:
                    seed_map[category] = {}
                    current_categories = line_categories
        elif line and line[0].isdigit():
            destination_range, source_range, range_length = [
                int(num) for num in line.split()]
            print(range_length)
            s_category, d_category = current_categories
            if s_category not in seed_map[d_category]:
                seed_map[d_category][s_category] = {}
            for i in range(range_length):
                seed_map[d_category][s_category][source_range +
                                                 i] = destination_range + i
        elif not line:
            current_categories = []
    return seed_map


def find_lowest_location(seed_map: dict, seeds: list) -> int:
    categories = ['soil', 'fertilizer', 'water',
                  'light', 'temperature', 'humidity', 'location']
    locations = []
    for seed in seeds:
        current_value = seed
        for i in range(len(categories)):
            if i == 0:
                source_category = 'seed'
            else:
                source_category = categories[i-1]
            destination_category = categories[i]
            if current_value in seed_map[destination_category][source_category]:
                current_value = seed_map[destination_category][source_category][current_value]
        locations.append(current_value)
    return min(locations)


def main():
    paths = ['test.txt', 'input.txt']
    for path in paths:
        content = read_input(path)
        seed_map = create_map(content)
        seeds = [int(seed)
                 for seed in content[0].split(":")[1].strip().split()]
        solution = find_lowest_location(seed_map, seeds)
        print(f"The lowest location number in {path}: {solution}")


if __name__ == "__main__":
    main()
