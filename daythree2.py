def lpn(start, end): #lpn stands for largest palindromic number
    for num in range(end, start - 1, -1):
        if str(num) == str(num)[::-1]:
            return num
    return None

start = 100
end = 200
print(lpn(start, end))
