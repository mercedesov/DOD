def print_triangle(height):
    for i in range(1, height + 1, 2):
        print('*' * i)

def user_input():
    height = int(input("Enter the height (odd number 1 to 10): "))
    if height > 0 and height <= 10 and height % 2 != 0:
        print_triangle(height)
    else:
        print("Error: Height must be an odd number 1 to 10")

user_input()
