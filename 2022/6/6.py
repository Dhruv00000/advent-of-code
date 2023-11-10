with open("6.txt", "r") as Input:

    stream = Input.read()

for i, code in enumerate(stream, start=0):

    characters = [code]

    for I in range(3):

        try:

            characters.append(stream[i + I + 1])

        except IndexError:

            break

    if len(characters) == 4 and len(set(characters)) == 4:

        print(i + I + 2)
        break

for e, Code in enumerate(stream, start=0):

    Characters = [Code]

    for E in range(13):

        try:

            Characters.append(stream[e + E + 1])

        except IndexError:

            break

    if len(Characters) == 14 and len(set(Characters)) == 14:

        print(e + E + 2)
        break

Input.close()