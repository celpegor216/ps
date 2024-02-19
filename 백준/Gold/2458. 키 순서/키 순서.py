from collections import deque

N, M = map(int, input().split())

children = [set() for _ in range(N + 1)]
parent = [set() for _ in range(N + 1)]
children_cnt = [0] * (N + 1)
parent_cnt = [0] * (N + 1)

for m in range(M):
    a, b = map(int, input().split())

    children[b].add(a)
    children_cnt[b] += 1
    parent[a].add(b)
    parent_cnt[a] += 1

q = deque()

for n in range(1, N + 1):
    if not children_cnt[n]:
        q.append(n)

children_result = children[:]
while q:
    now = q.popleft()

    for p in parent[now]:
        children_result[p].update(children_result[now])
        children_cnt[p] -= 1

        if not children_cnt[p]:
            q.append(p)

q = deque()

for n in range(1, N + 1):
    if not parent_cnt[n]:
        q.append(n)

parent_result = parent[:]
while q:
    now = q.popleft()

    for c in children[now]:
        parent_result[c].update(parent_result[now])
        parent_cnt[c] -= 1

        if not parent_cnt[c]:
            q.append(c)

result = 0
for n in range(1, N + 1):
    if len(children_result[n]) + len(parent_result[n]) == N - 1:
        result += 1

print(result)