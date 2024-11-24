from json import loads as json_loads

with open("input", "r") as inputText:
    json = inputText.read()

numbers_concatenated: str = ""
previous_digit: int = -1 # -1 is just a placeholder because initializing the variable without any assigned value results in an error.

for i in range(len(json)):

    if json[i] in ["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        numbers_concatenated += json[i]
        previous_digit = i

    elif i - 1 == previous_digit: numbers_concatenated += ";"

print(sum(map(int, (numbers_concatenated).split(";")[1:-1]))) # The list is spliced from 1 to -1 because the first and last elements of the split list are empty strings.

def sum_NonRed(object):
    if isinstance(object, dict):

        if "red" in object.values(): return 0

        return sum(map(sum_NonRed, object.values()))

    if isinstance(object, list):
        return sum(map(sum_NonRed, object))

    if isinstance(object, int): return object

    return 0

print(sum_NonRed(json_loads(json)))