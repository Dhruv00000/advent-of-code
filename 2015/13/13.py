from itertools import permutations

with open("input", "r") as inputText:
    happiness_conditions = inputText.readlines()

arrangements = tuple(permutations(("Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory")))

happiness_values: dict[tuple[str, str], int] = {}
for condition in happiness_conditions:

    words = condition.split()

    if "gain" in words: happiness = int(words[3])
    else: happiness = - int(words[3])

    happiness_values[(words[0], words[-1].rstrip()[:-1])] = happiness

possibile_happiness_values: set[int] = set()
possibile_happiness_values_part2: set[int] = set()
for arrangement in arrangements:
    total_happiness = 0
    happiness_changes = set()

    for i in range(len(arrangement)):

        happiness_change = happiness_values[(arrangement[i], arrangement[i - 1])] + happiness_values[(arrangement[i - 1], arrangement[i])] # happiness conditions are defined for ordered pairs.

        total_happiness += happiness_change
        happiness_changes.add(happiness_change)

    total_happiness_part2 = total_happiness - min(happiness_changes) # Instead of generating new permutations and finding the optimal arrangement again, in order to get an optimal arrangement, we can just place a gap in between the two people who reduce the total happiness the most.

    possibile_happiness_values.add(total_happiness)
    possibile_happiness_values_part2.add(total_happiness_part2)

print(max(possibile_happiness_values))
print(max(possibile_happiness_values_part2))