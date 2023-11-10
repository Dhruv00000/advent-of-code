with open("9.txt", "r") as Input:

    lines = Input.readlines()

x,y, X,Y, visited = 0,0, 0,0, []

for line in lines:

    for _ in range(int(line[2])):

        if line[0] == "U":

            y += 1

        elif line[0] == "D":

            y -= 1

        elif line[0] == "R":

            x += 1

        else:

            x -= 1

        if x == X + 1:

            X += 1

            if y == Y + 2:

                y += 1

            elif y == Y - 2:

                y -= 1

        elif x == X - 1:

            X -= 1

            if y == Y + 2:

                Y += 1

            elif y == Y - 2:

                Y -= 1

        elif x == X:

            if y == Y + 2:

                y += 1

            elif y == Y - 2:

                y -= 1

        elif y == Y + 1:

            Y += 1

            if x == X + 2:

                X += 1

            elif x == X - 2:

                X -= 1

        elif y == Y - 1:

            Y -= 1

            if x == X + 2:

                X += 1

            elif x == X - 2:

                X -= 1

        elif y == Y:

            if x == X + 2:

                X += 1

            elif x == X - 2:

                X -= 1

        visited.append(f"{X} {Y}")

print(len(set(visited)))

Input.close()