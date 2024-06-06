import random

def mask_number(input):
    """the program chooses the mask between
    '*' and 'X' randomly"""

    parts = input.split()
    if len(parts) == 1:
        number = parts[0]
    else:
        number = ''.join(parts)

    if len(number) <= 4:
        return number

    mask = random.choice(['*', 'X'])
    masked = mask * (len(number) - 4)

    if len(parts) == 1:
        return masked + number[-4:]
    else:
        return ' '.join(masked[i:i + 4] for i in range(0, len(masked), 4)) + ' ' + number[-4:]

print(mask_number("1234 5678 1234 5678"))
print(mask_number("52310259"))
