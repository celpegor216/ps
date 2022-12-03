from collections import deque

N, M = map(int, input().split())

moves = {}

for i in range(N + M):
    start, end = map(int, input().split())
    moves.update({start: end})

def bfs():
    q = deque()
    used = [0] * 101

    q.append((1, 0))
    used[1] = 1

    while q:
        nown, nowc = q.popleft()

        if nown == 100:
            return nowc

        for i in range(1, 7):
            nextn = nown + i
            if 0 < nextn <= 100 and not used[nextn]:
                used[nextn] = 1
                if nextn in moves.keys():
                    q.append((moves[nextn], nowc + 1))
                else:
                    q.append((nextn, nowc + 1))

print(bfs())