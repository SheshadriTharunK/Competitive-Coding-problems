start_date = (2000, 1, 1)
year1, month1, day = start_date
days = int(input())

day += days
while True:
    if month1 in [1, 3, 5, 7, 8, 10, 12]:
        days_month = 31
    elif month1 in [4, 6, 9, 11]:
        days_month = 30
    else:
        if year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0):
            days_month = 29
        else:
            days_month = 28

    if day > days_month:
        day -= days_month
        month1 += 1
    else:
        break

    if month1 > 12:
        month1 = 1
        year1 += 1
date = "{:02d}-{:02d}-{:02d}".format(year1, month1, day)
print(date)
