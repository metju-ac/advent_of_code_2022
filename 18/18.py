from collections import deque


def load_data():
    cubes = []
    maxes = [0, 0, 0]
    with open("18.txt", "r") as f:
        for line in f:
            line = line.strip().split(",")
            line = list(map(int, line))

            for i in range(3):
                maxes[i] = max(maxes[i], line[i])

            cubes.append(tuple(line))
    return cubes, maxes


def get_neighbours(cube):
    x, y, z = cube
    neighbours = []
    for i in [-1, 1]:
        neighbours.append((x + i, y, z))
        neighbours.append((x, y + i, z))
        neighbours.append((x, y, z + i))
    return neighbours


def first(cubes):
    res = 0

    for cube in cubes:
        touching = 0
        for neighbour in get_neighbours(cube):
            if neighbour in cubes:
                touching += 1

        res += 6 - touching

    return res


def second(cubes, maxes):
    res = 0
    max_x, max_y, max_z = maxes

    q = deque()
    q.append((-1, -1, -1))
    water = set()

    while q:
        x, y, z = q.popleft()
        if (x, y, z) in water:
            continue
        water.add((x, y, z))

        for neigh_x, neigh_y, neigh_z in get_neighbours((x, y, z)):
            if -1 <= neigh_x <= max_x + 1 and -1 <= neigh_y <= max_y + 1 and -1 <= neigh_z <= max_z + 1:
                if (neigh_x, neigh_y, neigh_z) not in cubes:
                    q.append((neigh_x, neigh_y, neigh_z))
                else:
                    res += 1

    return res


if __name__ == '__main__':
    data, m = load_data()
    print(first(data))
    print(second(data, m))
