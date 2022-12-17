from collections import deque
from copy import deepcopy


class Square:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.visited = False
        self.distance = 0
        self.start = False

        if val == "E":
            self.value = ord("z") - ord("a")
            self.visited = True
        elif val == "S":
            self.value = 0
            self.start = True
        else:
            self.value = ord(val) - ord("a")


def load_data():
    grid = []
    lowest = []

    with open("12.txt", "r") as f:
        for y, line in enumerate(f):
            cur_line = []
            for x, char in enumerate(line.strip()):
                cur_line.append(Square(x, y, char))
                if char == "E":
                    end = (x, y)
                elif char == "a":
                    lowest.append((x, y))
            grid.append(cur_line)

    return grid, end


def get_neighbours(grid, x, y):
    cur_distance = grid[y][x].distance
    cur_value = grid[y][x].value
    neighbours = []

    if x >= 1 and not grid[y][x - 1].visited and (grid[y][x - 1].value - cur_value) >= -1:
        neighbours.append((x - 1, y))
        grid[y][x - 1].visited = True
        grid[y][x - 1].distance = cur_distance + 1
    if x <= len(grid[0]) - 2 and not grid[y][x + 1].visited and (grid[y][x + 1].value - cur_value) >= -1:
        neighbours.append((x + 1, y))
        grid[y][x + 1].visited = True
        grid[y][x + 1].distance = cur_distance + 1
    if y >= 1 and not grid[y - 1][x].visited and (grid[y - 1][x].value - cur_value) >= -1:
        neighbours.append((x, y - 1))
        grid[y - 1][x].visited = True
        grid[y - 1][x].distance = cur_distance + 1
    if y <= len(grid) - 2 and not grid[y + 1][x].visited and (grid[y + 1][x].value - cur_value) >= -1:
        neighbours.append((x, y + 1))
        grid[y + 1][x].visited = True
        grid[y + 1][x].distance = cur_distance + 1

    return neighbours


def bfs(grid, position, first):
    end_x, end_y = position
    queue = deque([(end_x, end_y)])

    while queue:
        x, y = queue.popleft()
        if first and grid[y][x].start:
            return grid[y][x].distance
        elif not first and grid[y][x].value == 0:
            return grid[y][x].distance
        queue.extend(get_neighbours(grid, x, y))


def first(grid, position):
    return bfs(grid, position, True)


def second(grid, position):
    return bfs(grid, position, False)


if __name__ == '__main__':
    data, pos = load_data()
    print(first(deepcopy(data), pos))
    print(second(data, pos))
