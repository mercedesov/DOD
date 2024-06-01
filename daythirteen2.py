def is_curzon(num):
    power = 2 ** num + 1
    multiply = 2 * num + 1
    return power % multiply == 0

print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))
