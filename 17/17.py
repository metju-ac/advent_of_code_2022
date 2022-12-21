def load_data():
    lefts = []
    with open("17.txt", "r") as f:
        for line in f:
            for char in line.strip():
                if char == "<":
                    lefts.append(True)
                else:
                    lefts.append(False)
    return lefts


def get_rock(rnd, h):
    if rnd % 5 == 0:
        return [(x, h + 4) for x in range(2, 6)]
    if rnd % 5 == 1:
        return [(3, h + 6), (2, h + 5), (3, h + 5), (4, h + 5), (3, h + 4)]
    if rnd % 5 == 2:
        return [(4, h + 6), (4, h + 5), (4, h + 4), (3, h + 4), (2, h + 4)]
    if rnd % 5 == 3:
        return [(2, h + y) for y in range(7, 3, -1)]
    if rnd % 5 == 4:
        return [(2, h + 5), (3, h + 5), (2, h + 4), (3, h + 4)]


def go_sideways(rocks, rock, left):
    move = -1 if left else 1
    for x, y in rock:
        if x + move < 0 or x + move >= 7:
            return
        if (x + move, y) in rocks:
            return

    for i in range(len(rock)):
        x, y = rock[i]
        rock[i] = (x + move, y)


def go_down(rocks, rock):
    for x, y in rock:
        if (x, y - 1) in rocks:
            return False
        if y == 1:
            return False

    for i in range(len(rock)):
        x, y = rock[i]
        rock[i] = (x, y - 1)

    return True


def solve(lefts, rounds):
    height = 0
    rocks = set()
    i = 0
    col_heights = [0 for _ in range(7)]
    history = {}

    rnd = 0
    while rnd < rounds:
        rock = get_rock(rnd, height)
        rnd += 1
        while True:
            go_sideways(rocks, rock, lefts[i])
            i += 1
            i %= len(lefts)
            if not go_down(rocks, rock):
                for x, y in rock:
                    rocks.add((x, y))
                    col_heights[x] = max(col_heights[x], y)

                height = max(col_heights)
                silhouette = [height - y for y in col_heights]

                if (tuple(silhouette), i, rnd % 5) in history:
                    prev_rnd, prev_height = history[tuple(silhouette), i, rnd % 5]
                    cycles = (rounds - rnd) // (rnd - prev_rnd)
                    rnd += cycles * (rnd - prev_rnd)
                    adding = cycles * (height - prev_height)
                    history = {}

                history[tuple(silhouette), i, rnd % 5] = (rnd, height)
                break

    return height + adding


def first(lefts):
    return solve(lefts, 2022)


def second(lefts):
    return solve(lefts, 1_000_000_000_000)


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
