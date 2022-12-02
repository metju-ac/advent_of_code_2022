def load_data():
    data = []
    with open("02.txt", "r") as f:
        for line in f:
            data.append(line.strip().split(" "))
    return data


def first_score(elf, me):
    if ord(elf) + 23 == ord(me):
        return 3
    if (elf == "A" and me == "Y") or \
       (elf == "B" and me == "Z") or \
       (elf == "C" and me == "X"):
        return 6
    return 0


def first(data):
    score  = 0
    for turn in data:
        elf, me = turn[0], turn[1]
        score += first_score(elf, me)
        score += ord(me) - 87
    return score


def second_score(elf, win):
    if win == "X":
        if elf == "A":
            return 3
        return ord(elf) - 65
    if win == "Y":
        return ord(elf) - 61
    if elf in ("A", "B"):
        return ord(elf) - 57
    return 7


def second(data):
    score = 0
    for turn in data:
        elf, me = turn[0], turn[1]
        score += second_score(elf, me)
    return score


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))