with open("input", "r") as inputText:
    strings = inputText.readlines()

difference: int = 0
difference_encoded: int = 0
for string in strings:

    string = string.rstrip()
    difference += len(string) - len(eval(string))

    difference_encoded += 2
    difference_encoded += string.count('"')
    difference_encoded += string.count('\\')

print(difference)
print(difference_encoded)