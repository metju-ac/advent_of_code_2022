def load_data():
    data = []
    with open("04.txt", "r") as f:
        for line in f:
            line = line.strip().split(",")
            line[0] = line[0].split("-")
            line[1] = line[1].split("-")
            for i in range(len(line)):
                line[i] = list(map(int, line[i]))
            data.append(line)
    return data

def first(data):
    count = 0
    for fst, snd in data:
        if (fst[0] <= snd[0] and fst[1] >= snd[1]) \
        or (snd[0] <= fst[0] and snd[1] >= fst[1]):
            count += 1
    return count


def second(data):
    count = 0
    for fst, snd in data:
        if (fst[0] <= snd[1] <= fst[1]) or (snd[0] <= fst[1] <= snd[1]):
            count += 1
    return count


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))