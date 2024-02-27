import heapq

N, M = map(int, input().split())
types = [''] + input().split()
groups = [n for n in range(N + 1)]
q = []

for _ in range(M):
    u, v, d = map(int, input().split())

    heapq.heappush(q, (d, u, v))

def find(a):
    if groups[a] != a:
        groups[a] = find(groups[a])
    return groups[a]

result = 0

def union(u, v, d):
    global result

    if types[u] == types[v]:
        return
    
    group_u, group_v = find(u), find(v)
    
    if group_u != group_v:
        groups[group_u] = group_v
        result += d

while q:
    d, u, v = heapq.heappop(q)
    union(u, v, d)

flag = 0
check = find(1)
for n in range(2, N + 1):
    if check != find(n):
        flag = 1
        break

if flag:
    print(-1)
else:
    print(result)