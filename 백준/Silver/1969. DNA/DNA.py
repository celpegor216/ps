N, M = map(int, input().split())
lst = [input() for _ in range(N)]

result = 0

for m in range(M):
    tmp = [0] * 26

    for n in range(N):
        tmp[ord(lst[n][m]) - ord('A')] += 1
    
    maxv = 0
    maxidx = 0

    for i in range(26):
        if tmp[i] > maxv:
            maxv = tmp[i]
            maxidx = i
    
    result += N - maxv
    print(chr(ord('A') + maxidx), end='')

print()
print(result)