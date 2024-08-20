S = input()
bucket = [0] * 26
for s in S:
    bucket[ord(s) - ord('A')] += 1

middle = -1
result = ''
for i in range(26):
    if bucket[i] % 2:
        if middle != -1:
            result = ''
            middle = -1
            break
        else:
            middle = i
        bucket[i] -= 1
    result += chr(ord('A') + i) * (bucket[i] // 2)

if not result:
    if middle == -1:
        print("I'm Sorry Hansoo")
    else:
        print(chr(ord('A') + middle))
else:
    if middle != -1:
        print(result + chr(ord('A') + middle) + result[::-1])
    else:
        print(result + result[::-1])