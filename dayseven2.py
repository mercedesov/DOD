import re

user_input = input("input a string: ")

vowels_list = re.compile(r'[aeiouAEIOU]')
consonants_list = re.compile(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]')

vowels = len(vowels_list.findall(user_input))
consonants = len(consonants_list.findall(user_input))

print(f"vowels: {vowels}")
print(f"consonants: {consonants}")