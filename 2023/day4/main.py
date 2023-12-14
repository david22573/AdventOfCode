from collections import defaultdict


def read_input(file: str):
    with open(f'day4/{file}') as f:
        return [line.strip() for line in f.readlines()]


def caclulate_points(content: list):
    p1 = 0
    N = defaultdict(int)
    for i, line in enumerate(content):
        N[i] += 1
        winning, rest = line.split('|')
        id_, card = winning.split(':')
        winning_nums = [int(x) for x in card.split()]
        rest_nums = [int(x) for x in rest.split()]
        val = len(set(winning_nums) & set(rest_nums))

        if val > 0:
            p1 += 2**(val-1)
        for j in range(val):
            N[i+j+1] += N[i]

    from pprint import pprint
    pprint(N)
    return sum(N.values())


def main():
    paths = ['test.txt', 'input.txt']

    for path in paths:
        content = read_input(path)
        solution = caclulate_points(content)
        print(f"The sum of all part numbers in {path}: {solution}")
        # break


if __name__ == "__main__":
    main()
