from collections import deque

F, S, G, U, D = map(int, input().split())

q = deque()
used = [0] * (F + 1)

result = 'use the stairs'

q.append((S, 0))
used[S] = 1

while q:
    now, cnt = q.popleft()

    if now == G:
        result = cnt
        break

    if 1 <= now + U <= F and not used[now + U]:
        q.append((now + U, cnt + 1))
        used[now + U] = 1
    
    if 1 <= now - D <= F and not used[now - D]:
        q.append((now - D, cnt + 1))
        used[now - D] = 1

print(result)