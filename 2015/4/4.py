from hashlib import md5

puzzle_input = "ckczppom"

solved_1: bool = False
solved_2: bool = False
iterator: int = 0
while not solved_2 or not solved_1:

    hash_value = md5((puzzle_input + str(iterator)).encode(encoding = "utf-8")).hexdigest()

    if not solved_1 and hash_value[:5] == "00000":
        print("part 1: ", iterator)
        solved_1 = True

    if not solved_2 and hash_value[:7] == "000000":
        print("part 2: ", iterator)
        solved_2 = True

    iterator += 1