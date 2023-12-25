from collections import deque

N = int(input())
lst = list(map(int, input().split()))

used = [21e8] * N
used[0] = 0

q = deque()
q.append((0, 0))

while q:
    now, cnt = q.popleft()

    if used[now] < cnt:
        continue

    if now == N - 1:
        break

    for i in range(1, lst[now] + 1):
        if now + i >= N:
            break

        if used[now + i] > cnt + 1:
            used[now + i] = cnt + 1
            q.append((now + i, cnt + 1))

if used[-1] == 21e8:
    print(-1)
else:
    print(used[-1])