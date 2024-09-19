from collections import deque


N, M = map(int, input().split())
lst = list(map(int, input().split()))

q = deque()
q.append((-1, 1, 0))   # 위치, 크기, 시간

result = 0
while q:
    pos, size, time = q.popleft()

    if time == M or pos == N - 1:
        result = max(result, size)
        continue

    if pos + 1 < N:
        q.append((pos + 1, size + lst[pos + 1], time + 1))
    if pos + 2 < N:
        q.append((pos + 2, size // 2 + lst[pos + 2], time + 1))

print(result)