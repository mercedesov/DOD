def is_pangram(text):
    unique = set()

    for char in text:
        if char.isalpha():
            unique.add(char.lower())

    return len(unique) == 26

text = input()

print(is_pangram(text))

print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))
