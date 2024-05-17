from collections import deque

N, K = map(int, input().split())
lines = [input() for _ in range(2)]

q = deque()
q.append((0, 0, 0))

used = [[0] * N for _ in range(2)]
used[0][0] = 1

result = 0

while q:
    nowc, nowl, nown = q.popleft()

    if nown + 1 >= N:
        result = 1
        break
    elif lines[nowl][nown + 1] == '1' and not used[nowl][nown + 1]:
        q.append((nowc + 1, nowl, nown + 1))
        used[nowl][nown + 1] = 1
    
    if nown - 1 > nowc and lines[nowl][nown - 1] == '1' and not used[nowl][nown - 1]:
        q.append((nowc + 1, nowl, nown - 1))
        used[nowl][nown - 1] = 1
    
    oppl = 1 if nowl == 0 else 0
    if nown + K >= N:
        result = 1
        break
    elif lines[oppl][nown + K] == '1' and not used[oppl][nown + K]:
        q.append((nowc + 1, oppl, nown + K))
        used[oppl][nown + K] = 1

print(result)