# 힌트: 위상정렬

from collections import deque

N = int(input())
lst = sorted(input().split())
M = int(input())

parents = [0] * N
children = [[] for _ in range(N)]

for _ in range(M):
    child, parent = input().split()
    cidx = lst.index(child)
    pidx = lst.index(parent)

    parents[cidx] += 1
    children[pidx].append(cidx)

result_roots = []
result_parents = [-1] * N
result_children = [[] for _ in range(N)]

q = deque()
for n in range(N):
    if not parents[n]:
        q.append(n)
        result_roots.append(n)

while q:
    now = q.popleft()

    for child in children[now]:
        result_parents[child] = now
        parents[child] -= 1

        if not parents[child]:
            result_children[now].append(child)
            q.append(child)

print(len(result_roots))

for root in result_roots:
    print(lst[root], end=' ')
print()

for n in range(N):
    print(lst[n], len(result_children[n]), *[lst[x] for x in sorted(result_children[n])])