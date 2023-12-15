def read_input(path: str) -> list:
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]


def main():
    paths = ['test.txt', 'input.txt']

    for path in paths:
        content = read_input(path)
        solution = None
        print(f"The sum of all part numbers in {path}: {solution}")
        # break


if __name__ == "__main__":
    main()
