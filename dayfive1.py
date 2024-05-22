def is_magic(date):
    day, month, year = map(int, date.split('.'))
    return day * month == year % 100

date = input()

print(is_magic(date))
