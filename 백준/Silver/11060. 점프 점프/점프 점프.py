from collections import deque

N = int(input())
lst = list(map(int, input().split()))

q = deque()
q.append((0, 0))

used = [0] * N
used[0] = 1

result = -1
while q:
    now, cnt = q.popleft()

    if now == N - 1:
        result = cnt
        break

    for i in range(1, lst[now] + 1):
        nxt = now + i
        
        if nxt >= N:
            break

        if not used[nxt]:
            used[nxt] = 1
            q.append((nxt, cnt + 1))

print(result)