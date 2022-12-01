def load_data():
    data = []
    with open("02.txt", "r") as f:
        cur_elf = 0
        for line in f:
            data.append(int(line.strip()))

    return data


def first(data):
    pass


def second(data):
    pass


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))