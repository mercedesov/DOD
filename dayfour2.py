def pascals_triangle(n):
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(prow[j-1] + prow[j])
            row.append(1)
        prow = row
        print(row)
