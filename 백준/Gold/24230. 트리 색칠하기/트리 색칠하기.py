import sys
input = sys.stdin.readline


N = int(input())
target_colors = [0] + list(map(int, input().split()))

lst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

parent = [0] * (N + 1)
parent[1] = -1

result_colors = [0] * (N + 1)

result = 0

q = [1]
while q:
    nq = []

    for now in q:
        if target_colors[now] != result_colors[now]:
            result_colors[now] = target_colors[now]
            result += 1

        for nxt in lst[now]:
            if parent[nxt]:
                continue

            parent[nxt] = now
            result_colors[nxt] = result_colors[now]
            nq.append(nxt)

    q = nq

print(result)