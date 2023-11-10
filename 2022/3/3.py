with open("3.txt", "r") as Input:

    lines = Input.readlines()

priorities = {

    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52

}
priority = 0

for line in lines:

    sLine = line.strip()
    first, second = sLine[:len(sLine)//2], sLine[len(sLine)//2:]

    for item in first:

        if item not in second:

            priority += priorities[item]
            break

print(priority)
print()

group, groups, Priority = [], [], 0

for Line in lines:

    SLine = Line.strip()
    group.append(SLine)

    if len(group) == 3:

        groups.append(group)
        group = []

for Group in groups:

    Priority += priorities[list(set(Group[0]).intersection(set(Group[1])).intersection(set(Group[2])))[0]]

print(Priority)
Input.close()