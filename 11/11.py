from copy import deepcopy


class Monkey:
    def __init__(self, items, operation, test, tru, fal):
        self.items = items
        self.operation = operation
        self.test = test
        self.tru = tru
        self.fal = fal
        self.inspections = 0

    def calculate(self, item):
        if self.operation[1].isnumeric():
            if self.operation[0] == "+":
                return item + int(self.operation[1])
            return item * int(self.operation[1])
        return item * item

    def test_item(self, item):
        return item % self.test == 0

    def inspect(self):
        self.inspections += 1

        item = self.items.pop(0)
        item = self.calculate(item)
        item //= 3

        if self.test_item(item):
            return item, self.tru
        return item, self.fal

    def second_inspect(self, modulo):
        self.inspections += 1

        item = self.items.pop(0)
        item = self.calculate(item)
        if modulo:
            item %= modulo
        else:
            item //= 3

        if self.test_item(item):
            return item, self.tru
        return item, self.fal


def load_data():
    lines = []
    monkeys = []
    modulo = 1

    with open("11.txt", "r") as f:
        for line in f:
            lines.append(line.strip())

    for i in range(0, len(lines), 7):
        items = lines[i + 1].split(":")[1].split(",")
        items = list(map(int, items))

        operation = lines[i + 2].split(" = ")[1].split(" ")[1:]

        test = int(lines[i + 3].split(" ")[-1])
        modulo *= test

        tru = int(lines[i + 4].split(" ")[-1])
        fal = int(lines[i + 5].split(" ")[-1])

        monkeys.append(Monkey(items, operation, test, tru, fal))

    return monkeys, modulo


def solve(monkeys, modulo=None):
    for _ in range(10000 if modulo else 20):
        for monkey in monkeys:
            while monkey.items:
                item, index = monkey.second_inspect(modulo)
                monkeys[index].items.append(item)

    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.inspections)
    inspections.sort()

    return inspections[-1] * inspections[-2]


def first(monkeys):
    return solve(monkeys)


def second(monkeys, modulo):
    return solve(monkeys, modulo)


if __name__ == '__main__':
    data, mod = load_data()
    print(first(deepcopy(data)))
    print(second(data, mod))
