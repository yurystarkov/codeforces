from collections import namedtuple

Position = namedtuple("Position", ["i", "j"], defaults=[None, None])


def find_start(matrix) -> Position:
    for i, string in enumerate(matrix):
        for j, element in enumerate(string):
            if element == "1":
                return Position(i, j)
    return Position()


matrix = [input().split() for _ in range(5)]

start = find_start(matrix)
finish = Position(2, 2)

print(abs(start.i - finish.i) + abs(start.j - finish.j))
