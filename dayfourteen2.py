def pythagorean_triples(diff, low, high):
    triples = []
    for a in range(low, high + 1):
        b = (a * a - diff * diff) // (2 * diff)
        c = b + diff
        if a * a + b * b == c * c:
            triples.append((a, b, c))
    return triples

print(pythagorean_triples(1, 2, 10))
print(pythagorean_triples(3, 10, 25))
print(pythagorean_triples(4, 100, 100))
print(pythagorean_triples(10, 91, 99))
