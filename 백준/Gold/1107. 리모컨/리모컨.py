from collections import deque

N = int(input())
M = int(input())
buttons = set(x for x in range(10))
if M:
    broken = set(map(int, input().split()))
    buttons -= broken

maxv = 10 ** 6

q = deque()
used = [0] * (maxv + 1)

result = abs(100 - N)

for n in buttons:
    q.append((n, 1))
    used[n] = 1

while q:
    now, cnt = q.popleft()

    result = min(result, abs(now - N) + cnt)

    if now == N:
        continue

    for n in buttons:
        tmp = now * 10 + n
        if tmp <= maxv and not used[tmp]:
            q.append((tmp, cnt + 1))
            used[tmp] = 1

print(result)