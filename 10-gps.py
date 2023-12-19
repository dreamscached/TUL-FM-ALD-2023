# NOTE: Graded 100/100
# NOTE: All tests pass

import pprint
import sys

IN_CITIES = [
    "liberec",
    "ceska-lipa",
    "chrastava",
    "new-york",
    "turnov",
    "jablonec-nad-nisou"
]

IN_TIMES = [
    [999, 999, 12, 24, 22, 20],
    [999, 999, 40, 10, 52, 999],
    [12, 40, 999, 20, 999, 999],
    [24, 10, 20, 999, 15, 30],
    [22, 52, 999, 15, 999, 22],
    [20, 999, 999, 30, 22, 999]
]

IN_DISTANCES = [
    [999, 999, 10, 35, 26, 20],
    [999, 999, 47, 30, 67, 999],
    [10, 47, 999, 14, 999, 999],
    [35, 30, 14, 999, 40, 30],
    [26, 67, 999, 40, 999, 24],
    [20, 999, 999, 30, 24, 999]
]

path_db = dict()

for idx, city in enumerate(IN_CITIES):
    ln_t = dict(filter(lambda it: it[1] != 999, map(lambda a, b: (b, a), IN_TIMES[idx], IN_CITIES)))
    ln_d = dict(filter(lambda it: it[1] != 999, map(lambda a, b: (b, a), IN_DISTANCES[idx], IN_CITIES)))
    path_db[city] = (ln_t, ln_d)

def pathfind(_from, to, _type):
    def traverse(path, _from, to, _type):
        destinations = path_db[_from][_type].keys()
        found_paths = list()

        for dest in destinations:
            if dest in path:
                continue

            found_paths.append(path)
            found_paths.extend(traverse([*path, dest], dest, to, _type))

        return found_paths

    def get_score(path, _type):
        node = path_db[path.pop(0)][_type]
        score = 0

        while path:
            _next = path.pop(0)
            distance = node[_next]
            score += distance
            node = path_db[_next][_type]

        return score

    all_paths = traverse([_from], _from, to, _type)
    all_paths = filter(lambda it: it and it[-1] == to, all_paths)
    all_paths = map(lambda it: (it, get_score(list(it), 0), get_score(list(it), 1)), all_paths)

    return list(all_paths)

for line in sys.stdin:
    _from, to, _type = line.strip().split(" ")
    _type = ["nejlepsi", "nejkratsi"].index(_type)

    ret = pathfind(_from, to, _type)
    ret = sorted(ret, key=lambda it: it[_type + 1])
    best = ret[0]

    print(f"({best[1]} min, {best[2]} km) {' -> '.join(best[0])}")