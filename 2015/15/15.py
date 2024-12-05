with open("input", "r") as inputText:
    ingredients = inputText.readlines()

stats: list[tuple[int, int, int, int, int]] = []
for ingredient in ingredients:
    words = ingredient.split()
    stats.append((int(words[2][:-1]), int(words[4][:-1]), int(words[6][:-1]), int(words[8][:-1]), int(words[10])))

maximum_score = 0
maximum_score_calories = 0
for sprinklesCount in range(101):
    for butterscotchCount in range(101 - sprinklesCount):
        for chocolateCount in range(101 - sprinklesCount - butterscotchCount):
            candyCount = 100 - sprinklesCount - chocolateCount - butterscotchCount 

            score = 1

            capacity = (stats[0][0] * sprinklesCount) + (stats[1][0] * butterscotchCount) + (stats[2][0] * chocolateCount) + (stats[3][0] * candyCount)
            durability = (stats[0][1] * sprinklesCount) + (stats[1][1] * butterscotchCount) + (stats[2][1] * chocolateCount) + (stats[3][1] * candyCount)
            flavour = (stats[0][2] * sprinklesCount) + (stats[1][2] * butterscotchCount) + (stats[2][2] * chocolateCount) + (stats[3][2] * candyCount)
            texture = (stats[0][3] * sprinklesCount) + (stats[1][3] * butterscotchCount) + (stats[2][3] * chocolateCount) + (stats[3][3] * candyCount)
            calories = (stats[0][4] * sprinklesCount) + (stats[1][4] * butterscotchCount) + (stats[2][4] * chocolateCount) + (stats[3][4] * candyCount)

            if durability <= 0 or capacity <= 0 or flavour <= 0 or texture <= 0: continue

            score *= capacity * flavour * texture * durability
            maximum_score = max(maximum_score, score)

            if calories == 500: maximum_score_calories = max(score, maximum_score_calories)

print(maximum_score)
print(maximum_score_calories)