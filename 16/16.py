from copy import deepcopy
from collections import deque


class Valve:
    def __init__(self, name, flow, tunnels):
        self.name = name
        self.flow = flow
        self.tunnels = tunnels
        self.open = False
        self.visited = False
        self.distance = 0


def load_data():
    valves = {}
    with open("16.txt", "r") as f:
        for line in f:
            line = line.split(" ")

            name = line[1]
            flow = int(line[4].split("=")[1][:-1])
            tunnels = []
            for i in range(9, len(line)):
                tunnels.append(line[i][:-1])

            valves[name] = Valve(name, flow, tunnels)
    return valves


def get_distances(valves):
    distances = {}

    for start in valves.keys():
        copied = deepcopy(valves)
        queue = deque()
        queue.append(copied[start])
        copied[start].visited = True

        while queue:
            cur = queue.popleft()
            for tunnel in cur.tunnels:
                if not copied[tunnel].visited:
                    queue.append(copied[tunnel])
                    copied[tunnel].visited = True
                    copied[tunnel].distance = cur.distance + 1

        for valve in copied.values():
            distances[(start, valve.name)] = valve.distance

    return distances


def filter_valves(valves, distances):
    valves = {k: v for k, v in valves.items() if v.flow != 0}

    start_distances = {k[1]: v for k, v in distances.items() if k[0] == "AA" and k[1] != "AA" and k[1] in valves.keys()}
    distances = {k: v for k, v in distances.items() if k[0] in valves.keys() and k[1] in valves.keys()}

    for valve in valves.values():
        valve.tunnels = [t for t in valve.tunnels if t in start_distances.keys()]

    return valves, distances, start_distances


def release_pressure(cur_valve, valves, distances, min_left, released):
    cur_valve.open = True
    min_left -= 1
    released += cur_valve.flow * min_left

    best = 0
    for start, tunnel in distances.keys():
        if start != cur_valve.name:
            continue
        if not valves[tunnel].open and distances[(cur_valve.name, tunnel)] < min_left:
            score = release_pressure(valves[tunnel], valves, distances, min_left - distances[(cur_valve.name, tunnel)],
                                     released,)
            best = max(best, score)

    cur_valve.open = False

    return max(best, released)


def solve(valves, distances, start_distances, time):
    best = 0
    for start, distance in start_distances.items():
        best = max(best, release_pressure(valves[start], valves, distances, time - distance, 0))

    return best


def split(valves, distances, start_distances, num):
    valves_me, valves_ele = {}, {}
    valves = list(valves.items())
    valves_me[valves[0][0]] = valves[0][1]

    for k, v in valves[1:]:
        if num % 2 == 0:
            valves_me[k] = v
        else:
            valves_ele[k] = v
        num //= 2

    distances_me = {k: v for k, v in distances.items() if k[0] in valves_me.keys() and k[1] in valves_me.keys()}
    start_distances_me = {k: v for k, v in start_distances.items() if k in valves_me.keys()}

    distances_ele = {k: v for k, v in distances.items() if k[0] in valves_ele.keys() and k[1] in valves_ele.keys()}
    start_distances_ele = {k: v for k, v in start_distances.items() if k in valves_ele.keys()}

    return valves_me, distances_me, start_distances_me, valves_ele, distances_ele, start_distances_ele


def first(valves, distances, start_distances):
    return solve(valves, distances, start_distances, 30)


def second(valves, distances, start_distances):
    best = 0

    for i in range(2 ** (len(start_distances) - 1)):
        valves_me, distances_me, start_distances_me, valves_ele, distances_ele, start_distances_ele = split(valves, distances, start_distances, i)
        score_me = solve(valves_me, distances_me, start_distances_me, 26)
        score_ele = solve(valves_ele, distances_ele, start_distances_ele, 26)
        best = max(best, score_me + score_ele)
    return best


if __name__ == '__main__':
    data = load_data()

    dist = get_distances(data)
    data, dist, start_dist = filter_valves(data, dist)

    print(first(data, dist, start_dist))
    print(second(data, dist, start_dist))
