input_string = input("Please insert a string of space-separated natural numbers")

numbers = list(map(int, input_string.split()))

if len(numbers) > 1:
    last_element = numbers.pop()
    numbers.insert(0, last_element)

print(" ".join(map(str, numbers)))