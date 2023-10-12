def rebuild(n):
    rim_dict = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L",
                40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    rim_num = ""
    for i in rim_dict:
        while n >= i:
            rim_num += rim_dict[i]
            n -= i
    return rim_num


n = int(input('Введите арабское число: '))
answer = rebuild(n)
print("Римское число:", answer)