from sympy import symbols, solve, Eq


def load_data():
    monkeys = {}
    with open("21.txt", "r") as f:
        for line in f:
            line = line.strip().split(": ")
            monkeys[line[0]] = line[1]
    return monkeys


def evaluate(job, values):
    if job.isnumeric():
        return int(job)

    job = job.split(" ")
    if job[0] not in values.keys() or job[2] not in values.keys():
        return

    if job[1] == "+":
        return values[job[0]] + values[job[2]]
    elif job[1] == "-":
        return values[job[0]] - values[job[2]]
    elif job[1] == "*":
        return values[job[0]] * values[job[2]]
    elif job[1] == "/":
        return values[job[0]] // values[job[2]]


def first(monkeys):
    values = {}
    while True:
        for monkey, job in monkeys.items():
            if monkey in values.keys():
                continue

            value = evaluate(job, values)
            if value is not None:
                if monkey == "root":
                    return value
                values[monkey] = value


def as_tree(monkeys, name):
    if name == "humn":
        return symbols("x")

    job = monkeys[name]
    if job.isnumeric():
        return int(job)

    job = job.split(" ")
    left = as_tree(monkeys, job[0])
    right = as_tree(monkeys, job[2])

    if job[1] == "+":
        return left + right
    elif job[1] == "-":
        return left - right
    elif job[1] == "*":
        return left * right
    elif job[1] == "/":
        return left / right


def second(monkeys):
    root = monkeys["root"].split(" ")
    left = as_tree(monkeys, root[0])
    right = as_tree(monkeys, root[2])
    equation = Eq(left - right, 0)
    return solve(equation)[0]


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
