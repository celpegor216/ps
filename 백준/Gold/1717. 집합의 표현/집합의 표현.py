N, M = map(int, input().split())
groups = [x for x in range(N + 1)]

def find(x):
    if groups[x] != x:
        groups[x] = find(groups[x])
    return groups[x]

def union(x, y):
    groups[find(y)] = find(x)

for m in range(M):
    command, x, y = map(int, input().split())
    
    if not command:
        union(x, y)
    else:
        print("yes") if find(x) == find(y) else print("no")