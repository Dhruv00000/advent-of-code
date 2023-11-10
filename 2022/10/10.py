# with open("10.txt", "r") as Input:

#     lines = Input.readlines()

# cycle, x, strengthSum, cycles = 0, 1, 0, [19,20, 59,60, 99,100, 139,140, 179,180, 219,220]

# for line in lines:

#     Line = line.strip()

#     if line.startswith("n"):

#         cycle += 1

#     else:

#         additive = int(Line.split(" ")[1])
#         cycle += 2
#         x += additive

#     if cycle in cycles:

#         if cycle % 2 != 0:

#             strength = (cycle + 1) * x
#             cycles.remove(cycle + 1)

#         else:

#             strength = cycle * x

#         strengthSum += strength

# # print(strengthSum)

# Input.close()