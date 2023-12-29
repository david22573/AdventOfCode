from solution import Solution


def read_input(path: str) -> list:
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]


def main():
    paths = ['test.txt', 'input.txt']
    for path in paths:
        content = read_input(path)
        solution = Solution(content).solve(part_two=True)
        print(f"The lowest location number in {path}: {solution}")


if __name__ == "__main__":
    main()
