s = input()

now = s[0]
total = 26 if now == 'c' else 10
num = total

for i in range(1, len(s)):
    if now == s[i]:
        num = 25 if s[i] == 'c' else 9
    else:
        now = s[i]
        num = 26 if s[i] == 'c' else 10
    total *= num

print(total)