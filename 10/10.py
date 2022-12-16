def load_data():
    data = []
    with open("10.txt", "r") as f:
        for line in f:
            line = line.strip().split(" ")
            if line[0] == "addx":
                data.append(["addx", 0])
            data.append(line)
    return data


def first(instructions):
    res = 0
    cycle = 0
    countdown = 20
    x = 1

    for instruction in instructions:
        cycle += 1
        countdown -= 1

        if countdown == 0:
            countdown = 40
            res += x * cycle

        if len(instruction) == 2:
            x += int(instruction[1])

    return res


def second(instructions):
    cycle = 0
    x = 2

    for instruction in instructions:
        cycle += 1
        if abs(x - cycle) <= 1:
            print("#", end="")
        else:
            print(".", end="")

        if cycle == 40:
            cycle = 0
            print()

        if len(instruction) == 2:
            x += int(instruction[1])



if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))