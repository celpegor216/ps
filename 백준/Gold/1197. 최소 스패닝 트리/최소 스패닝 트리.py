# 크루스칼
# 구현은 해답 참조함

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

group = [i for i in range(V + 1)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(y, x, e):
    global total, cnt
    group_y, group_x = find(y), find(x)
    
    if group_y != group_x:
        total += edges[e][2]
        
        if group_x < group_y:
            group[group_y] = group_x
        else:
            group[group_x] = group_y
            

total = 0
for e in range(E):
    union(edges[e][0], edges[e][1], e)
    
print(total)