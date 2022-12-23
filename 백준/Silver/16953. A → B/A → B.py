from collections import deque

A, B = map(int, input().split())

def bfs():
    q = deque()
    q.append((A, 1))

    used = []
    used.append(A)

    while q:
        nowv, nowc = q.popleft()

        if nowv == B:
            return nowc
        elif nowv < B:
            q.append((nowv * 2, nowc + 1))
            q.append((nowv * 10 + 1, nowc + 1))

    return -1

print(bfs())