# TODO: Use functions.
with open("input", "r") as directionsText:
    directions = directionsText.readline()

santaX, santaY, roboX, roboY, deliveredTo, deliveredToCopy = (
    0,
    0,
    0,
    0,
    [(0, 0)],
    [(0, 0)],
)


def move(delivererX, delivererY, step, toAppend):
    if step == "<":
        delivererX -= 1
    elif step == ">":
        delivererX += 1
    elif step == "^":
        delivererY += 1
    else:
        delivererY -= 1

    toAppend.append((delivererX, delivererY))


for step in directions:
    if step == "<":
        santaX -= 1
    elif step == ">":
        santaX += 1
    elif step == "^":
        santaY += 1
    else:
        santaY -= 1

    deliveredTo.append((santaX, santaY))

print(len(set(deliveredTo)))

santaX, santaY = 0, 0
for i, step in enumerate(directions):
    if i % 2 == 1:
        if step == "<":
            santaX -= 1
        elif step == ">":
            santaX += 1
        elif step == "^":
            santaY += 1
        else:
            santaY -= 1

        deliveredToCopy.append((santaX, santaY))

    else:
        if step == "<":
            roboX -= 1
        elif step == ">":
            roboX += 1
        elif step == "^":
            roboY += 1
        else:
            roboY -= 1

        deliveredToCopy.append((roboX, roboY))

print(len(set(deliveredToCopy)))

directionsText.close()
