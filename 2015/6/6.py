import numpy

with open("input", "r") as inputText:
    instructions = inputText.readlines()

grid_BinaryState: numpy.ndarray = numpy.zeros((1000, 1000), dtype = numpy.int8)
grid_LightLevel: numpy.ndarray = numpy.zeros((1000, 1000), dtype = numpy.int8)

for instruction in instructions:

    splitList = instruction.split(" through ")
    secondConer: list[str] = splitList[1].split(",")
    firstCorner: list[str] = splitList[0].split(" ")[-1].split(",")

    mode: str = splitList[0].split(" ")[1]
    del(splitList)

    # for some reason, using a variable like
    # rectangle = grid[int(firstCorner[1]) : int(secondConer[1].rstrip()) + 1, int(firstCorner[0]) : int(secondConer[0]) + 1]
    # for this extremly long expression doesnt work
    if mode == "on":
        grid_BinaryState[int(firstCorner[1]) : int(secondConer[1].rstrip()) + 1, int(firstCorner[0]) : int(secondConer[0]) + 1] = 1
        grid_LightLevel[int(firstCorner[1]) : int(secondConer[1].rstrip()) + 1, int(firstCorner[0]) : int(secondConer[0]) + 1] += 1

    elif mode == "off":
        grid_BinaryState[int(firstCorner[1]) : int(secondConer[1].rstrip()) + 1, int(firstCorner[0]) : int(secondConer[0]) + 1] = 0
        grid_LightLevel[int(firstCorner[1]) : int(secondConer[1].rstrip()) + 1, int(firstCorner[0]) : int(secondConer[0]) + 1] -= 1

    else:

        # floor(cos(integer)) inverts 1s and 0s, and binary complement doesn't work here because there is no 1 bit integer dataype.
        grid_BinaryState[int(firstCorner[1]) : int(secondConer[1].rstrip()) + 1, int(firstCorner[0]) : int(secondConer[0]) + 1] = numpy.floor(numpy.cos(grid_BinaryState[int(firstCorner[1]) : int(secondConer[1].rstrip()) + 1, int(firstCorner[0]) : int(secondConer[0]) + 1]))

        grid_LightLevel[int(firstCorner[1]) : int(secondConer[1].rstrip()) + 1, int(firstCorner[0]) : int(secondConer[0]) + 1] += 2

    grid_LightLevel[grid_LightLevel == -1] = 0 # brightness levels stop going down after 0.

unique, counts = numpy.unique(grid_BinaryState, return_counts = True)
print(dict(zip(unique, counts))[numpy.int8(1)])

print(numpy.sum(grid_LightLevel))