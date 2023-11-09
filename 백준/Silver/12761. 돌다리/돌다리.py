from collections import deque

A, B, N, M = map(int, input().split())

q = deque()
q.append((N, 0))

used = [21e8] * 100001
used[N] = 0

result = 21e8

while q:
    nown, nowc = q.popleft()

    if nown == M:
        result = nowc
        break

    for tmp in (nown + 1, nown - 1, nown + A, nown - A, nown + B, nown - B, nown * A, nown * B):
        if 0 <= tmp <= 100000 and nowc + 1 < used[tmp]:
            used[tmp] = nowc + 1
            q.append((tmp, nowc + 1))
    
print(result)