def F(dct, x):
    answer = []
    for key, value in dct.items():
        if key == x:
            answer.append(value)
        elif isinstance(value, dict):
            answer.extend(F(value,x))
    return answer

dct = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11}, 6: 22}
print(F(dct, 3))

