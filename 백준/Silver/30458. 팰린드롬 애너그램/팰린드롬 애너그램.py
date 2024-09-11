N = int(input())
S = input()

bucket = [0] * 26
for s in S:
    bucket[ord(s) - ord('a')] += 1

if N % 2:
    bucket[ord(S[N // 2]) - ord('a')] -= 1

for i in range(26):
    if bucket[i] % 2:
        print('No')
        break
else:
    print('Yes')