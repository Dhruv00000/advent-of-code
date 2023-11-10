with open("7.txt", "r") as Input:

    lines = Input.readlines()

total,Total = 0,0

for line in lines:

    if line.startswith("$ ls"):

        if total <= 100000:

            Total += total

        total = 0

    try:

        total += int(line.split(" ")[0])

    except ValueError:

        continue

print(Total)

Input.close()