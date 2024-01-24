# 한붓그리기인 건 알겠는데 한붓그리기 조건을 모름
# 해답: https://devlibrary00108.tistory.com/429

V, E = map(int, input().split())
lst = [0] * (V + 1)
group = [x for x in range(V + 1)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        group[group_b] = group_a

for e in range(E):
    a, b = map(int, input().split())
    
    lst[a] += 1
    lst[b] += 1

    union(a, b)

result = 'YES'

now = find(group[1])
for v in range(2, V + 1):
    if now != find(group[v]):
        result = 'NO'
        break

if result == 'YES':
    cnt = 0
    for v in range(1, V + 1):
        if lst[v] % 2:
            cnt += 1
    
    if cnt not in (0, 2):
        result = 'NO'

print(result)