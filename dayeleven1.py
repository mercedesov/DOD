def remove_duplicates(num):
    checked = set()
    unique = []

    for n in num:
        if n not in checked:
            checked.add(n)
            unique.append(n)

    return unique


num = [57, 94, 4, 4, 4, 41, 65, 94, 4, 99, 9, 9, 94]
print(remove_duplicates(num))