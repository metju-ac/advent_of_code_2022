def load_data():
    data = []
    with open("03.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def first(data):
    pass


def second(data):
    pass


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
