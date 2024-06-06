def swap(lst, pos1, pos2):
    lst[pos1 - 1], lst[pos2 - 1] = lst[pos2 - 1], lst[pos1 - 1]
    return lst

print(swap([23, 65, 19, 90], 1, 3))
print(swap([1, 2, 3, 4, 51], 2, 5))
