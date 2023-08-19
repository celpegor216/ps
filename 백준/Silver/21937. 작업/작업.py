from collections import deque

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    a, b = map(int, input().split())

    lst[b].append(a)

X = int(input())

q = deque()
q.append(X)
used = [0] * (N + 1)
used[X] = 1

result = set()
while q:
    now = q.popleft()

    for item in lst[now]:
        if not used[item]:
            used[item] = 1
            result.add(item)
            q.append(item)

print(len(result))