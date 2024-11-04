# import sys
# from itertools import permutations

# places = set()
# distances = {}
# for line in open('input'):
#     (source, _, dest, _, distance) = line.split()
#     places.add(source)
#     places.add(dest)
#     distances.setdefault(source, {})[dest] = int(distance)
#     distances.setdefault(dest, {})[source] = int(distance)

# shortest = sys.maxsize
# longest = 0
# for items in permutations(places):
#     dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
#     shortest = min(shortest, dist)
#     longest = max(longest, dist)

# print("shortest: %d" % (shortest))
# print("longest: %d" % (longest))

import itertools
import sys

with open("input", "r") as inputText:
    paths = inputText.readlines()

lines = (x.strip().split(" ")[::2] for x in paths)
routes = {frozenset(x[:2]): int(x[2]) for x in lines}
places = set.union(*(set(x) for x in routes))
path_len = lambda path: sum(routes[frozenset(x)] for x in zip(path, path[1:]))
lengths = [path_len(x) for x in itertools.permutations(places)]

print(min(lengths))
print(max(lengths))