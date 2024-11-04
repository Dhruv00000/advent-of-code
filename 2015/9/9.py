from itertools import permutations

with open("input", "r") as inputText:
    paths = inputText.readlines()

starting_locations: set = set()
ending_locations: set = set()

path_dict: dict = {}
for path in paths:

    splitList = path.split(" = ")
    distance: int = int(splitList[1])
    locations = splitList[0].split(" to ")
    del splitList

    starting_locations.add(locations[0])
    ending_locations.add(locations[1])

    path_dict[(locations[0], locations[1])] = distance

locations: set = starting_locations.union(ending_locations)

# The set difference operation gives a set of all locations that you can start at but not end at, or vice-versa. This allows us to determine which locations we must start and end at.
start: str = list(starting_locations - ending_locations)[0]
end: str = list(ending_locations - starting_locations)[0]
del starting_locations
del ending_locations

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