def max_sum(tuples):
    return max(tuples, key=sum)

tuples = [(1, 2, 3), (4, 1, 2), (2, 2, 2)]
print(max_sum(tuples))
