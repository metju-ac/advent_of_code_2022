def load_data():
    data = []
    with open("03.txt", "r") as f:
        for line in f:
            data.append(line.strip())
    return data


def get_score(item):
    if item.isupper():
        return ord(item) - ord("A") + 27
    return ord(item) - ord("a") + 1


def first(data):
    score = 0
    for rucksack in data:
        half = len(rucksack) // 2
        fst, snd = set(rucksack[:half]), rucksack[half:]
        for item in fst:
            if item in snd:
                score += get_score(item)
    return score


def second(data):
    score = 0
    for i in range(0, len(data), 3):
        fst, snd, trd = set(data[i]), data[i + 1], data[i + 2]
        for item in fst:
            if item in snd and item in trd:
                score += get_score(item)
    return score


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))