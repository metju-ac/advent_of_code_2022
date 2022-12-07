def load_data():
    data = []
    with open("07.txt", "r") as f:
        for line in f:
            data.append(line.strip().split(" "))
    return data


class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.size = 0
        self.dirs = []
        self.files = []


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def add_file(directory, size, name):
    f = File(name, size)
    directory.files.append(f)
    while directory:
        directory.size += int(size)
        directory = directory.parent


def add_directory(directory, name):
    d = Dir(directory, name)
    directory.dirs.append(d)
    return d


def is_cmd(line):
    return line[0] == "$"


def is_ls(line):
    return line[1] == "ls"


def is_cd(line):
    return line[1] == "cd"


def is_dir(line):
    return line[0] == "dir"


def parse_fs(lines):
    root = Dir(None, "/")
    current = root
    i = 0
    while i < len(lines):
        i += 1
        if is_ls(lines[i]):
            i += 1
            while i < len(lines) and not is_cmd(lines[i]):
                if not is_dir(lines[i]):
                    add_file(current, lines[i][0], lines[i][1])
                i += 1
            if i != len(lines):
                i -= 1
        else:
            if lines[i][-1] == "..":
                current = current.parent
            else:
                current = add_directory(current, lines[i][-1])

    return root


def size_sum(root, count):
    if root.size <= 100000:
        count += root.size
    for child in root.dirs:
        count = size_sum(child, count)
    return count


def find_smallest(root, space_needed, current_best):
    if space_needed <= root.size < current_best.size:
        current_best = root
    for child in root.dirs:
        current_best = find_smallest(child, space_needed, current_best)
    return current_best


def first(root):
    return size_sum(root, 0)


def second(root):
    space_needed = root.size - 40000000
    return find_smallest(root, space_needed, root).size


if __name__ == '__main__':
    r = parse_fs(load_data())
    print(first(r))
    print(second(r))
