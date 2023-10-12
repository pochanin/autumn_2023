from datetime import datetime


year = 2023
for month in range(1, 13):
    count_3 = 0
    for day in range(1, 22):
        if datetime(year, month, day).weekday() == 3:
            count_3 += 1
        if count_3 == 3:
            print(str(day) + '.' +str(month) + '.' + str(year))
            break