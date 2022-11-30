def load_data():
    data = []
    with open("01.txt", "r") as f:
        for line in f:
            data.append(int(line.strip()))
    return data

if __name__ == '__main__':
    data = load_data()
    print(data)