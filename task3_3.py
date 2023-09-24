words = input('Введите предложение: ').split()
lenth = [len(i) for i in words]
maxi = max(lenth)
for i in words:
    if len(i) == maxi:
        print(i)
