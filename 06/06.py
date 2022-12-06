from collections import deque


def load_data():
    with open("06.txt", "r") as f:
        data = f.read()
    return data


def solve(length, data):
    chars = deque(data[:length])
    for i in range(length, len(data)):
        if len(set(chars)) == length:
            return i
        chars.popleft()
        chars.append(data[i])


def first(data):
    return solve(4, data)


def second(data):
    return solve(14, data)


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))