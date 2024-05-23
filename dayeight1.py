str1 = input("Enter a string: ")

first_c = str1[0].upper()

middle = len(str1) // 2
middle_c = str1[middle].upper()

last_c = str1[-1].upper()

str2 = first_c + middle_c + last_c

print(str2)
