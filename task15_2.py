import re


def F(s):
    s1 = r"[ABCEHKMOPTXАВСЕНКМОРТХ]\d{3}[ABCEHKMOPTXАВСЕНКМОРТХ][ABCEHKMOPTXАВСЕНКМОРТХ]78|[ABCEHKMOPTXАВСЕНКМОРТХ]\d{3}[ABCEHKMOPTXАВСЕНКМОРТХ][ABCEHKMOPTXАВСЕНКМОРТХ]178"
    car = re.findall(s1, s)

    return car


check = 'M123OP78TX547НК178'

print(F(check))
