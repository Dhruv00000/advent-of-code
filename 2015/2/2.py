with open("input", "r") as text:
    inputText = text.readlines()

totalPaperRequirement, totalRibbonRequirement = 0, 0
for box in inputText:
    dimensions = box.split("x")

    tsa = 2 * (
        int(dimensions[0]) * int(dimensions[1])
        + int(dimensions[1]) * int(dimensions[2])
        + int(dimensions[2]) * int(dimensions[0])
    )
    paperRequirement = tsa + min(
        [
            (int(dimensions[0]) * int(dimensions[1])),
            (int(dimensions[1]) * int(dimensions[2])),
            (int(dimensions[2]) * int(dimensions[0])),
        ]
    )
    totalPaperRequirement += paperRequirement

    vol = int(dimensions[1]) * int(dimensions[2]) * int(dimensions[0])
    ribbonRequirement = vol + min(
        [
            2 * (int(dimensions[0]) + int(dimensions[1])),
            2 * (int(dimensions[1]) + int(dimensions[2])),
            2 * (int(dimensions[2]) + int(dimensions[0])),
        ]
    )
    totalRibbonRequirement += ribbonRequirement

print(totalPaperRequirement)
print(totalRibbonRequirement)
