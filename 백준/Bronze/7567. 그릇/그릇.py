s = input()

now = s[0]
result = 10

for i in range(1, len(s)):
    if s[i] == now:
        result += 5
    else:
        result += 10
        now = s[i]

print(result)