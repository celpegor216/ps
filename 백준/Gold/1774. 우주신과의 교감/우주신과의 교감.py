import heapq

N, M = map(int, input().split())
lst = [0] + [list(map(int, input().split())) for _ in range(N)]

q = []

for m in range(M):
    a, b = map(int, input().split())
    heapq.heappush(q, (0, a, b))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j:
            heapq.heappush(q, ((abs(lst[i][0] - lst[j][0]) ** 2 + abs(lst[i][1] - lst[j][1]) ** 2) ** 0.5, i, j))

group = [x for x in range(N + 1)]
result = 0

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b, c):
    global result

    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        group[group_b] = group_a
        result += c

while 1:
    c, a, b = heapq.heappop(q)

    union(a, b, c)

    flag = 0
    standard = find(1)
    for i in range(2, N + 1):
        if standard != find(i):
            flag = 1
            break
    
    if not flag:
        break

print(f'{result:0.2f}')