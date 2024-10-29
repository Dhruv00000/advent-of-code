with open("input", "r") as text:
    inputText = text.readlines()

paperRequirement: int = 0
ribbonRequirement: int = 0

for box in inputText:
    dimensions = box.split("x")

    areas: list[int] = [
            (int(dimensions[0]) * int(dimensions[1])),
            (int(dimensions[1]) * int(dimensions[2])),
            (int(dimensions[2]) * int(dimensions[0])),
        ]

    paperRequirement += 2 * sum(areas) + min(areas)
    ribbonRequirement += int(dimensions[1]) * int(dimensions[2]) * int(dimensions[0]) + min(
        [
            2 * (int(dimensions[0]) + int(dimensions[1])),
            2 * (int(dimensions[1]) + int(dimensions[2])),
            2 * (int(dimensions[2]) + int(dimensions[0])),
        ]
    )

print(paperRequirement)
print(ribbonRequirement)