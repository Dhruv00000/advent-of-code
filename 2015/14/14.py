with open("input", "r") as inputText:
    descriptions = inputText.readlines()

descriptions_dict: dict[str, tuple[int, int, int]] = {}
for description in descriptions:

    words = description.split()
    descriptions_dict[words[0]] = (int(words[3]), int(words[6]), int(words[-2]))

    current_time = 0
    distance = 0

distances: dict[str, int] = {"Rudolph": 0, "Cupid": 0, "Prancer": 0, "Donner": 0, "Dasher": 0, "Comet": 0, "Blitzen": 0, "Vixen": 0, "Dancer": 0}
flying_states: dict[str, bool] = {"Rudolph": True, "Cupid": True, "Prancer": True, "Donner": True, "Dasher": True, "Comet": True, "Blitzen": True, "Vixen": True, "Dancer": True}
timers: dict[str, int] = {"Rudolph": descriptions_dict["Rudolph"][1], "Cupid": descriptions_dict["Cupid"][1], "Prancer": descriptions_dict["Prancer"][1], "Donner": descriptions_dict["Donner"][1], "Dasher": descriptions_dict["Dasher"][1], "Comet": descriptions_dict["Comet"][1], "Blitzen": descriptions_dict["Blitzen"][1], "Vixen": descriptions_dict["Vixen"][1], "Dancer": descriptions_dict["Dancer"][1]}
scores: dict[str, int] = distances.copy()
for _ in range(2503):
    for name in descriptions_dict.keys():

        if flying_states[name]:
            distances[name] += descriptions_dict[name][0]
            timers[name] -= 1

            if timers[name] == 0:
                flying_states[name] = not flying_states[name]
                timers[name] = descriptions_dict[name][2]

        else:
            timers[name] -= 1
            if timers[name] == 0:
                flying_states[name] = not flying_states[name]
                timers[name] = descriptions_dict[name][1]

    max_distance = max(distances.values())
    for deer, distance in distances.items():
        if distance == max_distance:
            scores[deer] += 1

print(max(scores.values()))
print(max(distances.values()))