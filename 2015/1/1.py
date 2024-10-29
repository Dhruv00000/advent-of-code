with open("input", "r") as text:
    instructions = text.readline()

floor: int = 0
basementReached: bool = False
for position, step in enumerate(instructions):

    if step == "(":
        floor += 1
    else:
        floor -= 1

    if not basementReached and floor == -1:
        print(position + 1)
        basementReached = True

print(floor)