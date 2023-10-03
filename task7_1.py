def NOK(a, b):
    s = a * b
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        elif b > a:
            b = b % a
        else:
            break
    return s // (a + b)

M = [13, 20, 29]
nok = M[0]
for i in range(1, len(M)):
    nok = NOK(nok, M[i])

print(nok)