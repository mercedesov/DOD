def move_zeros(arr):
    result = []

    zeros = 0

    for num in arr:
        if num == 0:
            zeros += 1
        else:
            result.append(num)

    result.extend([0] * zeros)

    return result


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
