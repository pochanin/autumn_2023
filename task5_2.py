M = []
n = int(input("Введите число: "))
for i in range(1, round(n**(1/2)) +1):
    if n % i == 0:
        M.append(i)
        if i != n // i:
            M.append(n // i)
M.sort()
print("Делители: ", *M)