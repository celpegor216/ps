N = int(input())
bucket = [0] * 26

for n in range(N):
    s = input()
    bucket[ord(s[0]) - ord('a')] += 1

result = ''
for i in range(26):
    if bucket[i] >= 5:
        result += chr(ord('a') + i)

if not result:
    print('PREDAJA')
else:
    print(result)