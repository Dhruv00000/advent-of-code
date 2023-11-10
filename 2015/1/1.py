with open("input", "r") as text:
    instructions = text.readline()

floor, foundPos, pos = 0, False, 0
for step in instructions:
    pos += 1
    if step == "(":
        floor += 1
    else:
        floor -= 1

    if not foundPos and floor < 0:
        print(pos)
        foundPos = True

print(floor)

text.close()
