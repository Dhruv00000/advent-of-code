with open("input", "r") as directionsText:
    directions = directionsText.readline()

santaCoordinates: list[int] = [0, 0]
robotCoordinates: list[int] = [0, 0]
presentCount_part1: list[tuple[int]] = [(0, 0)]
presentCount_part2: list[tuple[int]] = [(0, 0)]

for step in directions:
    match step:
        case ">":
            santaCoordinates[0] += 1
        case "<":
            santaCoordinates[0] -= 1
        case "^":
            santaCoordinates[1] += 1
        case "v":
            santaCoordinates[1] -= 1

    if (santaCoordinates[0], santaCoordinates[1]) not in presentCount_part1:
        presentCount_part1.append((santaCoordinates[0], santaCoordinates[1]))

print(len(presentCount_part1))

santaCoordinates: list[int] = [0, 0] # santa's coordinates must be reset back to (0,0) before starting the first part because the same variable was used and modified in the first part.

for counter, step in enumerate(directions):

    if counter % 2 == 0:
        match step:
            case ">":
                santaCoordinates[0] += 1
            case "<":
                santaCoordinates[0] -= 1
            case "^":
                santaCoordinates[1] += 1
            case "v":
                santaCoordinates[1] -= 1

        if (santaCoordinates[0], santaCoordinates[1]) not in presentCount_part2:
            presentCount_part2.append((santaCoordinates[0], santaCoordinates[1]))

    else:
        match step:
            case ">":
                robotCoordinates[0] += 1
            case "<":
                robotCoordinates[0] -= 1
            case "^":
                robotCoordinates[1] += 1
            case "v":
                robotCoordinates[1] -= 1

        if (robotCoordinates[0], robotCoordinates[1]) not in presentCount_part2:
            presentCount_part2.append((robotCoordinates[0], robotCoordinates[1]))

print(len(presentCount_part2))