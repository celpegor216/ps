from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

lst = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    a, b, c = map(int, input().split())
    lst[a][b] = max(lst[a][b], c)

used = [[0] * (N + 1) for _ in range(M + 1)]
q = deque()
q.append((1, 1, 0))

result = 0

while q:
    nowm, nown, nowt = q.popleft()

    if nown == N:
        result = max(result, nowt)
        continue
    
    if nowm == M or used[nowm][nown] > nowt:
        continue

    for nextn in range(nown + 1, N + 1):
        if lst[nown][nextn] and used[nowm + 1][nextn] < nowt + lst[nown][nextn]:
            used[nowm + 1][nextn] = nowt + lst[nown][nextn]
            q.append((nowm + 1, nextn, nowt + lst[nown][nextn]))

print(result)