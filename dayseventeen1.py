def is_valid(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return not s

print(is_valid("()[]{}"))
print(is_valid("(]"))
