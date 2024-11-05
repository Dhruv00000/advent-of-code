num = "1321131112"

def process_digits() -> str:
    new_num: str = ""

    for i, digit in enumerate(num):

        j = i
        count: int = 1

        if i != len(num) - 1:
            while num[j + 1] == digit:
                count += 1
                j += 1
            if (i != 0 and num[i - 1] != digit) or i == 0: new_num += str(count) + digit

        else: new_num += f"1{digit}"

    return new_num

for i in range(50):

    num = process_digits()

    if i == 39: print(len(num))

print(len(num))