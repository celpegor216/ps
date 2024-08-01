# DP인줄 알았는데 BFS네...

from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    q = deque()
    visited = [0] * 100001

    q.append((N, 0))
    visited[N] = 1

    while q:
        nown, nowt = q.popleft()

        if nown == K:
            return nowt

        if 0 <= nown - 1 <= 100000 and not visited[nown - 1]:
            visited[nown - 1] = 1
            q.append((nown - 1, nowt + 1))

        if 0 <= nown + 1 <= 100000 and not visited[nown + 1]:
            visited[nown + 1] = 1
            q.append((nown + 1, nowt + 1))

        if 0 <= nown * 2 <= 100000 and not visited[nown * 2]:
            visited[nown * 2] = 1
            q.append((nown * 2, nowt + 1))

result = bfs(N, K)

print(result)