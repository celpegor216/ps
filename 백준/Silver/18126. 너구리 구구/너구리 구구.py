from collections import deque

N = int(input())
lst = [[] for _ in range(N + 1)]

# N - 1개 간선으로 모든 노드에 갈 수 있다 > 트리!
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

results = [0] * (N + 1)

q = deque()
q.append(1)

used = [0] * (N + 1)
used[1] = 1

while q:
    now = q.popleft()

    for nxt, cost in lst[now]:
        if used[nxt]:
            continue

        used[nxt] = 1
        results[nxt] = results[now] + cost
        q.append(nxt)

print(max(results))