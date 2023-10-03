alfabet_b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfabet_s = 'abcdefghijklmnopqrstuvwxyz'

n = int(input('Введите n: '))
s = input('Введите предложение: ')
n = n % 26
s1 = ''
for i in range(len(s)):
    if s[i] in alfabet_s:
        index = alfabet_s.index(s[i])
        s1 += alfabet_s[(n + index) % 26]
    elif s[i] in alfabet_b:
        index = alfabet_b.index(s[i])
        s1 += alfabet_b[(n + index) % 26]
    else:
        s1 += s[i]

print(s1)