def zeros(s):
   not_zero = 0

   for i in range(len(s)):
       if s[i] != 0:
           s[not_zero], s[i] = s[i], s[not_zero]
           not_zero += 1
   return s

s = [0, 1, 3, 0, 2]
print(zeros(s))
