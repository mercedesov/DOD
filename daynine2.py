n = int(input("Please insert the number of numbers in the set: "))

numbers = [int(input()) for _ in range(n)]

check_number = int(input("Please insert an integer to check if it's the product of two numbers from the set: "))

found = False

for i in range(n):
    for j in range(i + 1, n):
        if numbers[i] * numbers[j] == check_number:
            found = True
            break
    if found:
        break

if found:
    print("YES")
else:
    print("NO")
