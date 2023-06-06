from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

INF = 21e8
board = [[INF] * N for _ in range(N)]

board[r1][c1] = 0
q = deque()
q.append((r1, c1, 0))

answer = -1

while q:
    nowr, nowc, nowp = q.popleft()

    if nowr == r2 and nowc == c2:
        answer = nowp
        break

    for dr, dc in ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)):
        nr, nc = nowr + dr, nowc + dc
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == INF:
            board[nr][nc] = nowp + 1
            q.append((nr, nc, nowp + 1))

print(answer)