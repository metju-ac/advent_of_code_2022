def load_data():
    lines = []
    grid = set()
    max_y = 0

    with open("14.txt", "r") as f:
        for line in f:
            lines.append(line.strip().split(" -> "))

    for line in lines:
        for i in range(len(line) - 1):
            x1, y1 = list(map(int, line[i].split(",")))
            x2, y2 = list(map(int, line[i + 1].split(",")))

            max_y = max(max_y, y1, y2)

            x_vect = x2 - x1
            if x_vect != 0:
                x_vect //= abs(x_vect)
            y_vect = y2 - y1
            if y_vect != 0:
                y_vect //= abs(y_vect)

            while (x1, y1) != (x2, y2):
                grid.add((x1, y1))
                x1 += x_vect
                y1 += y_vect
            grid.add((x1, y1))

    return grid, max_y


def solve(grid, max_y, part_1):
    units = 0
    while True:
        sand_x, sand_y = 500, 0
        while True:
            moved = False

            if part_1 and sand_y > max_y:
                return units
            if not part_1 and sand_y == max_y + 1:
                grid.add((sand_x, sand_y))
                units += 1
                break

            for change_x in (0, -1, 1):
                if (sand_x + change_x, sand_y + 1) not in grid:
                    sand_x += change_x
                    sand_y += 1
                    moved = True
                    break

            if not moved:
                grid.add((sand_x, sand_y))
                units += 1
                if not part_1 and sand_y == 0:
                    return units
                break


def first(grid, max_y):
    return solve(grid, max_y, True)


def second(grid, max_y):
    return solve(grid, max_y, False)


if __name__ == '__main__':
    data, depth = load_data()
    print(first(data.copy(), depth))
    print(second(data, depth))
