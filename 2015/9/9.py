from itertools import permutations

with open("input", "r") as inputText:
    paths = inputText.readlines()

path_dict: dict = {}
locations: set[str] = set()
for path in paths:

    splitList = path.split(" = ")
    distance: int = int(splitList[1])
    cities = splitList[0].split(" to ")
    del splitList

    locations.add(cities[0])
    locations.add(cities[1])

    path_dict[(cities[0], cities[1])] = distance

del cities

path_lengths: set = set()
for path in permutations(locations):

    path_length: int = 0
    errored: bool = False

    for location in path[:-1]:

        try: path_length += path_dict[(location, path[path.index(location) + 1])]
        except KeyError: # some permutations do not exist, which causes a KeyError

            try: path_length += path_dict[(path[path.index(location) + 1], location)]
            except KeyError:
                errored = True
                break

    path_lengths.add(path_length)

print(min(path_lengths))
print(max(path_lengths))