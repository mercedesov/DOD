def length(s):
    def different(sus):
        return len(set(sus)) == len(sus)

    max_length = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if different(s[i:j]):
                max_length = max(max_length, j - i)

    return max_length

s = "abcabcbb"
print(length(s))