from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    A, B = map(int, input().split())
    lst[B].append(A)

max_cnt = 0
max_parents = []

for n in range(1, N + 1):
    q = deque()
    q.append(n)
    used = [0] * (N + 1)
    used[n] = 1
    total = 1

    while q:
        now = q.popleft()

        for item in lst[now]:
            if not used[item]:
                total += 1
                used[item] = 1
                q.append(item)

    if total > max_cnt:
        max_cnt = total
        max_parents = [n]
    elif total == max_cnt:
        max_parents.append(n)

print(*sorted(max_parents))