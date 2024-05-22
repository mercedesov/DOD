def print_squares(n):
    if n < 1 or n > 20:
        return

    for i in range(n):
        print(i ** 2)

d = int(input("Enter a number between 1 and 20: "))
print_squares(d)

