S = input()
K = input()

result = ''
for s in S:
    if '0' <= s <= '9':
        continue
    result += s

print(1 if K in result else 0)