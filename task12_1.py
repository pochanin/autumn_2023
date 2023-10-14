def F(X):
    Min = []
    Max = []
    for i in range(len(X)):
        if X[i] == min(X):
            Min.append(i)
        if X[i] == max(X):
            Max.append(i)
    return Min, Max


x = input('Введите числа через пробелы: ').split()
mini, maxi =F(x)
print(f'{mini}, {maxi}')

