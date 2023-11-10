with open("1.txt", "r") as Input:

    lines = Input.readlines()

elf = []
elves = []

for calorie in lines:

    if calorie == "\n":

        elves.append(elf)
        elf = []

    else:

        elf.append(int(calorie))

Input.close()

elfCalories = [sum(elf) for elf in elves]
top = []

print(max(elfCalories))

for _ in range(3):

    top.append(max(elfCalories))
    elfCalories.remove(max(elfCalories))

print(sum(top))