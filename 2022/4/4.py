with open("4.txt", "r") as Input:

    lines = Input.readlines()

commons,contained, overlap = 0,0, 0

for line in lines:

    pair = line.split(",")
    first,second, sections = pair[0].split("-"),(pair[1].strip()).split("-"), []
    checked = False

    sections.extend(iter(range(int(first[0]),int(first[1]) + 1)))

    for Section in range(int(second[0]),int(second[1]) + 1):

        if Section in sections:

            commons += 1

            if not checked:

                overlap += 1
                checked = True

    if commons in [len(range(int(first[0]),int(first[1]) + 1)), len(range(int(second[0]),int(second[1]) + 1))]:

        contained += 1

    commons = 0

print(contained)
print(overlap)
Input.close()