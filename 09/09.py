def load_data():
    data = []
    with open("09.txt", "r") as f:
        for line in f:
            data.append(line.strip().split(" "))
    return data


def move_head(head, direction):
    head_x, head_y = head

    if direction == "U":
        return head_x, head_y + 1
    elif direction == "D":
        return head_x, head_y - 1
    elif direction == "R":
        return head_x + 1, head_y
    return head_x - 1, head_y


def move_tail(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    x_dif = head_x - tail_x
    y_dif = head_y - tail_y

    if abs(x_dif) == 2 and abs(y_dif) == 2:
        if x_dif > 0:
            if y_dif > 0:
                return head_x - 1, head_y - 1
            return head_x - 1, head_y + 1

        if y_dif > 0:
            return head_x + 1, head_y - 1
        return head_x + 1, head_y + 1

    if x_dif == 2:
        return head_x - 1, head_y
    if x_dif == -2:
        return head_x + 1, head_y
    if y_dif == 2:
        return head_x, head_y - 1
    return head_x, head_y + 1


def touching(head, tail):
    head_x, head_y = head
    tail_x, tail_y = tail
    return abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1


def solve(length, instructions):
    knots = [(0, 0) for _ in range(length)]
    tail_positions = {(0, 0)}

    for direction, amount in instructions:
        for _ in range(int(amount)):
            knots[0] = move_head(knots[0], direction)
            for i in range(1, len(knots)):
                if not touching(knots[i - 1], knots[i]):
                    knots[i] = move_tail(knots[i - 1], knots[i])
            tail_positions.add(knots[-1])

    return len(tail_positions)


def first(instructions):
    return solve(2, instructions)


def second(instructions):
    return solve(10, instructions)


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
