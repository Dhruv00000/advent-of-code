with open("5.txt", "r") as Input:

    lines = Input.readlines()

steps, starting = [], []

for line in lines:

    if line.startswith("m"):

        steps.append(line.strip())

    else:

        starting.append(line.strip())

starting.remove("")
starting.remove(starting[-1])

one, two, three, four, five, six, seven, eight, nine = [
], [], [], [], [], [], [], [], []

for row in starting:

    if row[1] != " ":

        one.append(row[1])

    if row[5] != " ":

        two.append(row[5])

    if row[9] != " ":

        three.append(row[9])

    if row[13] != " ":

        four.append(row[13])

    if row[17] != " ":

        five.append(row[17])

    if row[21] != " ":

        six.append(row[21])

    if row[25] != " ":

        seven.append(row[25])

    try:

        if row[29] != " ":

            eight.append(row[29])

    except IndexError:

        eight.append(" ")

    try:

        if row[33] != " ":

            nine.append(row[33])

    except IndexError:

        nine.append(" ")

stacks = [one, two, three, four, five, six, seven, eight, nine]

for stack in stacks:

    while stack[0] == " ":

        stack.remove(" ")

for step in steps:

    Step = step.removeprefix("move ")
    step = Step.replace("from ", "")
    Step = step.replace("to ", "")

    references,References = Step.split(" "),[]
    References.extend(int(reference) for reference in references)

    for _ in range(References[0]):

        stacks[References[2] - 1].insert(0, stacks[References[1] - 1])
        stacks[References[1] - 1].pop(0)

Input.close()