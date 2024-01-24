import heapq

N = int(input())
stars = [list(map(float, input().split())) for _ in range(N)]

q = []

for i in range(N):
    for j in range(i + 1, N):
        a = abs(stars[i][0] - stars[j][0])
        b = abs(stars[i][1] - stars[j][1])

        heapq.heappush(q, ((a ** 2 + b ** 2) ** 0.5, i, j))

group = [x for x in range(N)]
result = 0

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b, c):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        group[group_b] = group_a
        return c
    return 0

while q:
    dist, a, b = heapq.heappop(q)

    result += union(a, b, dist)

print(result)