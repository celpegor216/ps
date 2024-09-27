import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0] + list(map(int, input().split()))
children = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    children[parent[i]].append(i)

result = [0] * (N + 1)
for _ in range(M):
    i, w = map(int, input().split())
    result[i] += w

q = [1]
while q:
    nq = []

    for now in q:
        for child in children[now]:
            result[child] += result[now]
            nq.append(child)

    q = nq

print(*result[1:])