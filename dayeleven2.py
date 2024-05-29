def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(anagrams(" python", " phtony"))
print(anagrams(" Java", " apaJ"))
print(anagrams(" 1234", " 2341"))
