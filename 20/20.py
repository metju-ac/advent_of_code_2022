def load_data():
    file = []
    with open("20.txt", "r") as f:
        for line in f:
            file.append(int(line.strip()))
    return file


def solve(file, rounds):
    indexes = list(range(len(file)))
    for _ in range(rounds):
        for i, num in enumerate(file):
            cur_pos = indexes.index(i)
            new_pos = (cur_pos + num) % (len(file) - 1)
            indexes.pop(cur_pos)
            indexes.insert(new_pos, i)

    zero = indexes.index(data.index(0))
    res = 0
    for i in (1000, 2000, 3000):
        res += file[indexes[(zero + i) % len(file)]]
    return res


def first(file):
    return solve(file, 1)


def second(file):
    file = [n * 811589153 for n in file]
    return solve(file, 10)


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
