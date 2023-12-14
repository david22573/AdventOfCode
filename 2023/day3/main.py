def read_input(file: str):
    with open(f'day3/{file}') as f:
        return [[c for c in line.strip()] for line in f.readlines()]


NONSYMBOLS = [str(i) for i in range(10)] + ['.']


def sum_part_numbers(content: list[str]):
    total_sum = 0

    numbers = ""
    adjacent_symbol = False

    symbol_positions = dict()
    pos = ''

    for y in range(len(content)):
        for x in range(len(content[y])):
            char = content[y][x]
            is_digit = char.isdigit()
            if is_digit:
                numbers += char
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if (dx != 0 or dy != 0) and 0 <= y + dy < len(content) and 0 <= x + dx < len(content[y]):
                            neighbor_char = content[y + dy][x + dx]
                            if neighbor_char == '*':
                                pos = f'({y + dy}, {x + dx})'
                                if pos not in symbol_positions:
                                    symbol_positions[pos] = []
                                adjacent_symbol = True
                                break
                    if adjacent_symbol:
                        break
            else:
                if numbers and adjacent_symbol:
                    if pos:
                        symbol_positions[pos].append(int(numbers))
                adjacent_symbol = False
                numbers = ""

    for nums in symbol_positions.values():
        if len(nums) == 2:
            sum = nums[0] * nums[1]
            total_sum += sum
    return total_sum


def main():
    paths = ['test.txt', 'input.txt']

    for path in paths:
        content = read_input(path)
        solution = sum_part_numbers(content)
        print(f"The sum of all part numbers in {path}: {solution}")
        # break


if __name__ == "__main__":
    main()
