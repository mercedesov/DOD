a = [89, 1, 60, 3, 89, 8, 13, 75, 21, 34, 1, 45, 55, 2, 15, 5]

result = []
for x in a:
    if x % 15 == 0:
        result.append(x)

print(result)
