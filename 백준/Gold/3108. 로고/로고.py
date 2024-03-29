N = int(input())
lst = [[set() for _ in range(1001)] for _ in range(1001)]    # 상, 우, 하, 좌

for n in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    x1 += 500
    y1 += 500
    x2 += 500
    y2 += 500

    # 가로
    for y in (y1, y2):
        for x in range(x1, x2 + 1):
            lst[y][x].add(n)
    
    # 세로
    for x in (x1, x2):
        for y in range(y1, y2 + 1):
            lst[y][x].add(n)

group = [x for x in range(N)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a < group_b:
        group[group_b] = group_a
    else:
        group[group_a] = group_b

for i in range(1001):
    for j in range(1001):
        if len(lst[i][j]) > 1:
            tmp = sorted(lst[i][j])
            for k in range(len(tmp)):
                for l in range(k + 1, len(tmp)):
                    union(tmp[k], tmp[l])

result = set()
for n in range(N):
    result.add(find(n))

if not lst[500][500]:
    print(len(result))
else:
    print(len(result) - 1)