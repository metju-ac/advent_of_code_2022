from collections import deque, defaultdict
from copy import deepcopy


def load_data():
    with open("05.txt", "r") as f:
        lines = f.read()
        data = lines.split("\n\n")
    return parse_stacks(data[0]), parse_instructions(data[1])


def parse_stacks(stacks):
    dic = defaultdict(deque)
    for line in stacks.split("\n"):
        for i, j in enumerate(range(0, len(line), 4)):
            char = line[j + 1]
            if char.isalpha():
                dic[i + 1].appendleft(char)
    return dic


def parse_instructions(instructions):
    res = []
    for line in instructions.split("\n"):
        line = line.split(" ")
        res.append((int(line[1]), int(line[3]), int(line[5])))
    return res


def get_result(dic):
    res = ""
    for i in range(len(dic)):
        res += dic[i + 1].pop()
    return res


def first(dic, instructions):
    for amount, fr, to in instructions:
        for _ in range(amount):
            dic[to].append(dic[fr].pop())
    return get_result(dic)


def second(dic, instructions):
    for amount, fr, to in instructions:
        picked = ""
        for _ in range(amount):
            picked += dic[fr].pop()
        dic[to].extend(reversed(picked))
    return get_result(dic)


if __name__ == '__main__':
    sta, ins = load_data()
    print(first(deepcopy(sta), ins))
    print(second(sta, ins))
