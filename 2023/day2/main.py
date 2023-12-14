# Cube Limits: 12 red cubes, 13 green cubes, and 14 blue cubes
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

INPUT_PATH = 'day2/input.txt'
TEST_PATH = 'day2/test.txt'

PATHS = (TEST_PATH, INPUT_PATH)

CUBE_LIMITS = {'red': 12, 'green': 13, 'blue': 14}


def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]

    return lines

# Part 1:
# def game_possible(cubes: list):
# for cube in cubes:
#     color, count = cube
#     if count > CUBE_LIMITS[color]:
#         return False
# return True

# Part 1:
# def extract_game_id(line: str):
# game_id = line[:line.find(':')].split(' ')[1]
# return int(game_id)


def extract_cubes(line: str):
    cubes = []
    cube_sets = line[line.find(':')+1:].strip().split(';')
    cube_sets = [cube.strip() for cube in cube_sets]
    for cube_line in cube_sets:
        cube_line = cube_line.split(',')
        for cube in cube_line:
            count, color = cube.strip().split(' ')
            count = int(count)
            cubes.append((color, count))
    return cubes

# def part1(lines):
#     id_sum = 0
#     for line in lines:
#         game_id = extract_game_id(line)
#         cubes = extract_cubes(line)
#         if game_possible(cubes):
#             id_sum += game_id
#     return id_sum


# Part 2:
def get_cube_power(cubes: list):
    colors = {'red': 0, 'green': 0, 'blue': 0}
    for color, count in cubes:
        if color in colors and count > colors[color]:
            colors[color] = count
    return colors['red'] * colors['green'] * colors['blue']


def part2(lines):
    power_sum = 0
    for line in lines:
        cubes = extract_cubes(line)
        cube_power = get_cube_power(cubes)
        power_sum += cube_power
    return power_sum


for path in PATHS:
    lines = read_input(path)
    # solution = part1(lines)
    print(path + '\n')
    solution = part2(lines)
    print(solution)
