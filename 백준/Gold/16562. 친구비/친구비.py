N, M, K = map(int, input().split())
cost = list(map(int, input().split()))

group = [n for n in range(N + 1)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        group[group_b] = group_a

for m in range(M):
    a, b = map(int, input().split())

    union(a, b)

pairs = [(n + 1, cost[n]) for n in range(N)]
pairs.sort(key=lambda x: x[1])

result = 0

for n in range(N):
    num, cost = pairs[n]
    if find(num) != 0:
        union(0, num)
        result += cost

if result <= K:
    print(result)
else:
    print("Oh no")