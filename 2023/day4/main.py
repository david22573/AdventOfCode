def read_input(file: str):
    with open(f'day4/{file}') as f:
        return [line.strip() for line in f.readlines()]


def caclulate_points(content: list):
    sum_points = 0
    instances = []
    for i in range(len(content)):
        matches = 0
        line = content[i]
        # card_id = line.split(':')[0].strip()
        # print(card_id)
        instances.append([line])
        all_numbers = line.split(':')[1].strip()
        winning_nums, numbers = [s.strip() for s in all_numbers.split('|')]
        winning_nums = [int(s) for s in winning_nums.split(' ') if s != '']
        numbers = [int(s) for s in numbers.split(' ') if s != '']

        for num in winning_nums:
            if num in numbers:
                matches += 1

        for j in range(matches):
            line = content[i+j+1]
            # card_id = line.split(':')[0].strip()
            instances.append([line])

    from pprint import pprint
    instances.sort()
    pprint(instances)

    return sum_points


def main():
    paths = ['test.txt', 'input.txt']

    for path in paths:
        content = read_input(path)
        solution = caclulate_points(content)
        print(f"The sum of all part numbers in {path}: {solution}")
        break


if __name__ == "__main__":
    main()
