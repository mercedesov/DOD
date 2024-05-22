def is_leap(year):
    if year % 4 != 0:
        return "Not leap"
    elif year % 100 == 0:
        if year % 400 == 0:
            return "Leap"
        else:
            return "Not leap"
    else:
        return "Leap"

year = int(input('Enter a year: '))
print(is_leap(year))

""" 
test = [1800, 1900, 2100, 2200, 2300, 2500]
for year in test:
    print(f"{year}: {is_leap(year)}")
"""