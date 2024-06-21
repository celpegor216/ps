import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))

kids = [1] * N
group = [n for n in range(N)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        if group_a > group_b:
            group_a, group_b = group_b, group_a
        group[group_b] = group_a
        kids[group_a] += kids[group_b]
        kids[group_b] = 0
        candies[group_a] += candies[group_b]
        candies[group_b] = 0

for _ in range(M):
    a, b = map(int, input().split())

    union(a - 1, b - 1)

groups = []

for n in range(N):
    if 0 < kids[n] < K:
        groups.append([kids[n], candies[n]])

groups.sort()

length = len(groups)
result = [[0] * (K) for _ in range(length)]

for i in range(length):
    for j in range(K):
        if j < groups[i][0]:
            result[i][j] = result[i - 1][j]
        else:
            result[i][j] = max(result[i - 1][j], result[i - 1][j - groups[i][0]] + groups[i][1])

print(max(result[-1]) if result else 0)