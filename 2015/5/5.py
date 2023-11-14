with open("input", "r") as inputText:
    strings = inputText.readlines()

niceStringCount, niceStringCount_alternate = 0, 0
for string in strings:
    (
        vowels,
        vowelRequirement,
        doubleLetterConsecutive,
        restrictedPhrasesContained,
        letterPairRepitition,
        letterRepition_alternate,
        letterPairsList,
    ) = (0, False, False, False, False, False, [])

    for i, char in enumerate(string):
        if not vowelRequirement and char in ["a", "e", "i", "o", "u"]:
            vowels += 1
            if vowels == 3:
                vowelRequirement = True

        if not doubleLetterConsecutive and char == string[i - 1]:
            doubleLetterConsecutive = True

        if i < len(string) - 2 and not letterPairRepitition and char != string[i - 1]:
            letterPairsList.append(f"{char}{string[i + 1].strip()}")

            if len(letterPairsList) != len(set(letterPairsList)):
                letterPairRepitition = True

        if (
            i < len(string) - 1
            and not letterRepition_alternate
            and string[i - 1] == string[i + 1]
        ):
            letterRepition_alternate = True

    for restrictedPhrase in ["ab", "cd", "pq", "xy"]:
        if restrictedPhrase in string:
            restrictedPhrasesContained = True
            break

    if not restrictedPhrasesContained and doubleLetterConsecutive and vowelRequirement:
        niceStringCount += 1
    if letterRepition_alternate and letterPairRepitition:
        niceStringCount_alternate += 1

print(niceStringCount)
print(niceStringCount_alternate)

inputText.close()
