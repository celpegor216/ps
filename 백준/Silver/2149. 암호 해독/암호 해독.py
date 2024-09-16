KEY = input()
S = input()
M = len(KEY)
N = len(S) // M

lst = [[''] * M for _ in range(N)]

idx = 0
for j in range(M):
    for i in range(N):
        lst[i][j] = S[idx]
        idx += 1

sorted_key = [(KEY[i], i) for i in range(M)]
sorted_key.sort()

result = ''
for i in range(N):
    tmp = [''] * M
    for j in range(M):
        tmp[sorted_key[j][1]] = lst[i][j]

    result += ''.join(tmp)

print(result)