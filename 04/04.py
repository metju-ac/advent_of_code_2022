def load_data():
    data = []
    with open("04.txt", "r") as f:
        for line in f:
            line = line.strip().replace(",", "-").split("-")
            line = list(map(int, line))
            data.append(line)
    return data


def first(data):
    count = 0
    for low_1, high_1, low_2, high_2 in data:
        if (low_1 <= low_2 and high_1 >= high_2) \
                or (low_2 <= low_1 and high_2 >= high_1):
            count += 1
    return count


def second(data):
    count = 0
    for low_1, high_1, low_2, high_2 in data:
        if low_2 <= high_1 and low_1 <= high_2:
            count += 1
    return count


if __name__ == '__main__':
    data = load_data()
    print(data)
    print(first(data))
    print(second(data))