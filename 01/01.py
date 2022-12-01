def load_data():
    data = []
    with open("01.txt", "r") as f:
        cur_elf = 0
        for line in f:
            if line.strip():
                cur_elf += int(line.strip())
            else:
                data.append(cur_elf)
                cur_elf = 0
    data.append(cur_elf)
    return data


def first(data):
    return max(data)


def second(data):
    return sum(sorted(data)[-3:])


if __name__ == '__main__':
    data = load_data()
    print(first(data))
    print(second(data))
