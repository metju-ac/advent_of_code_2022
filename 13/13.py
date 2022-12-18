def load_data():
    pairs = []
    with open("13.txt", "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 3):
        pairs.append([eval(lines[i]), eval(lines[i + 1])])
    return pairs


def cmp(l, r):
    if type(l) is int and type(r) is int:
        if l != r:
            return l < r

    elif type(l) is list and type(r) is list:
        for ll, rr in zip(l, r):
            compared = cmp(ll, rr)
            if compared is not None:
                return compared
        if len(l) != len(r):
            return len(l) < len(r)

    elif type(l) is list:
        return cmp(l, [r])

    else:
        return cmp([l], r)


def first(pairs):
    res = 0

    for i, (l, r) in enumerate(pairs):
        if cmp(l, r):
            res += i + 1

    return res


def second(pairs):
    new = []
    for l, r in pairs:
        new.append(l)
        new.append(r)

    fst, snd = 1, 2
    for pair in new:
        if cmp(pair, [[2]]):
            fst += 1
        if cmp(pair, [[6]]):
            snd += 1

    return fst * snd


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
