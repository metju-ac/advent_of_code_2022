def load_data():
    pairs = []
    with open("15.txt", "r") as f:
        for line in f:
            line += "."
            line = line.split(" ")
            pair = []
            for i in [2, 3, 8, 9]:
                pair.append(int(line[i][2:-1]))
            pairs.append(pair)
    return pairs


def get_distance(sensor_x, sensor_y, beacon_x, beacon_y):
    return abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)


def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if merged[-1][0] <= interval[0] <= merged[-1][-1]:
            merged[-1][-1] = max(merged[-1][-1], interval[-1])
        else:
            merged.append(interval)

    return merged


def count_intervals(intervals):
    count = 0

    for interval in intervals:
        count += interval[1] - interval[0]

    return count


def get_bounds(distance, x, y):
    bounds = []

    for i in range(distance):
        bounds.append((x - distance - 1 + i, y - i))
        bounds.append((x + distance + 1 - i, y - i))
        bounds.append((x - distance - 1 + i, y + i))
        bounds.append((x + distance + 1 - i, y + i))

    return bounds


def is_inside(x, y, pairs):
    for sensor_x, sensor_y, beacon_x, beacon_y in pairs:
        if get_distance(sensor_x, sensor_y, x, y) <= get_distance(sensor_x, sensor_y, beacon_x, beacon_y):
            return False
    return True


def first(pairs):
    intervals = []
    depth = 10

    for sensor_x, sensor_y, beacon_x, beacon_y in pairs:
        distance = get_distance(sensor_x, sensor_y, beacon_x, beacon_y)

        if abs(depth - sensor_y) > distance:
            continue

        width = abs(distance - abs(sensor_y - depth))
        intervals.append([sensor_x - width, sensor_x + width])

    merged = merge_intervals(intervals)
    return count_intervals(merged)


def second(pairs):
    size = 4_000_000
    for sensor_x, sensor_y, beacon_x, beacon_y in pairs:
        distance = get_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        bounds = get_bounds(distance, sensor_x, sensor_y)

        for x, y in bounds:
            if 0 <= x <= size and 0 <= y <= size and is_inside(x, y, pairs):
                return x * size + y


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
