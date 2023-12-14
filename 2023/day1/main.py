with open('day1/input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

with open('day1/test.txt') as f:
    test_lines = [line.strip() for line in f.readlines()]

total_sum = 0

alpha_nums = {"one": 1, "two": 2, "three": 3, "four": 4,
              "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def add_digits(line: str):
    nums = []
    for i in range(len(line)):
        char = line[i]
        if char.isdigit():
            nums.append(int(char))
        else:
            for k, v in alpha_nums.items():
                match_k = char + line[i+1:i+len(k)]
                if k == match_k:
                    nums.append(v)
    digits = f'{nums[0]}{nums[-1]}'
    return int(digits)


for line in lines:
    digits = add_digits(line)
    total_sum += digits

print(total_sum)
