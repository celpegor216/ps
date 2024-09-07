M = int(input())
S = input()
N = len(S)
N = N // M

lst = [[''] * M for _ in range(N)]
r = 0
ranges = (range(M), range(M - 1, -1, -1))
idx = 0
for n in range(N):
    for m in ranges[r]:
        lst[n][m] = S[idx]
        idx += 1
    r = 1 - r

for m in range(M):
    for n in range(N):
        print(lst[n][m], end='')