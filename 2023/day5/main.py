def read_input(path: str) -> list:
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]


class Solution:
    def __init__(self, content) -> None:
        self.content = content
        self.categories = []
        self.parse_content()

    def parse_content(self):
        content = self.content
        self.content = content

    def part_one(self):
        pass

    def part_two(self):
        pass


def main():
    paths = ['test.txt', 'input.txt']
    for path in paths:
        content = read_input(path)
        solution = None
        print(f"The lowest location number in {path}: {solution}")


if __name__ == "__main__":
    main()
