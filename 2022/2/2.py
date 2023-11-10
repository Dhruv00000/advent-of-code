with open("2.txt", "r") as Input:

    lines = Input.readlines()

playerScore = 0

for line in lines:

    moves = line.split()
    opponent, player = moves[0], moves[1]

    if opponent == "A" and player == "X":

        playerScore += 4

    elif opponent == "A" and player == "Y":

        playerScore += 8

    elif opponent == "A" and player == "Z":

        playerScore += 3

    elif opponent == "B" and player == "X":

        playerScore += 1

    elif opponent == "B" and player == "Y":

        playerScore += 5

    elif opponent == "B" and player == "Z":

        playerScore += 9

    elif opponent == "C" and player == "X":

        playerScore += 7

    elif opponent == "C" and player == "Y":

        playerScore += 2

    else:

        playerScore += 6

print(playerScore)

newScore = 0

for line in lines:

    data = line.split()
    Opponent, state = data[0], data[1]

    if Opponent == "A" and state == "X":

        newScore += 3

    elif Opponent == "A" and state == "Y":

        newScore += 4

    elif Opponent == "A" and state == "Z":

        newScore += 8

    elif Opponent == "B" and state == "X":

        newScore += 1

    elif Opponent == "B" and state == "Y":

        newScore += 5

    elif Opponent == "B" and state == "Z":

        newScore += 9

    elif Opponent == "C" and state == "X":

        newScore += 2

    elif Opponent == "C" and state == "Y":

        newScore += 6

    else:

        newScore += 7

print(newScore)
Input.close()