from collections import deque


N, K = map(int, input().split())
children = [[] for _ in range(N)]
for _ in range(N - 1):
    p, c = map(int, input().split())
    children[p].append(c)
has_apple = list(map(int, input().split()))

result = 0

q = deque()
q.append(0)

for _ in range(K + 1):
    for _ in range(len(q)):
        now = q.popleft()

        result += has_apple[now]

        for child in children[now]:
            q.append(child)

print(result)