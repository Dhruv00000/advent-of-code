# TODO: Create hashing algorithm instead of using haslib.
from hashlib import md5

fiveFound, sixFound = False, False
for potential in range(1, 2147483648):  # 2^31 (31-bit integer limit)
    if (
        md5(f"ckczppom{potential}".encode("UTF-8")).hexdigest()[:5] == "00000"
    ) and not fiveFound:
        print(potential)
        fiveFound = True

    if (
        md5(f"ckczppom{potential}".encode("UTF-8")).hexdigest()[:6] == "000000"
    ) and not sixFound:
        print(potential)
        sixFound = True

    if fiveFound and sixFound:
        break
