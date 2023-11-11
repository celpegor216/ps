from collections import deque

H, Y = map(int, input().split())

q = deque()
q.append((H, 0))

result = 0

while q:
    nowh, nowy = q.popleft()

    if nowy > Y:
        continue

    result = max(result, nowh)

    q.append((int(nowh * 1.05), nowy + 1))
    q.append((int(nowh * 1.2), nowy + 3 ))
    q.append((int(nowh * 1.35), nowy + 5))

print(result)