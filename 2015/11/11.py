password: str = "hxbxwxba"

def increment(string: str) -> str:

    if string == "z": return "a"
    if string[-1] == "z": return increment(string[:-1]) + "a"
    if len(string) == 1: return chr(ord(string) + 1)
    return string[0] + increment(string[1:])

def hasRepitition(string: str) -> bool:

    pairs_count: int = 0
    possible_overlap: int = 8

    for i in range(len(string) - 1):

        if string[i] == string[i + 1] and i != possible_overlap:
            pairs_count += 1
            possible_overlap = i + 1

        if pairs_count == 2:
            return True

    return False

def hasIncreasingSequence(string: str) -> bool:

    for i in range(1, len(string) - 1):
        if ord(string[i - 1]) + 1 == ord(string[i]) == ord(string[i + 1]) - 1:
            return True

    return False

passwords_count: int = 0
while passwords_count != 2:

    flag1: bool = "i" not in password and "l" not in password and "o" not in password

    if flag1 and hasIncreasingSequence(password) and hasRepitition(password):
        passwords_count += 1
        print(password)

    password = increment(password)
