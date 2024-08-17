# 문제를 잘못 읽고 루트가 1로 고정되어 있는 줄 알았음...

N = int(input())
lst = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N):
    p, c1, c2 = map(int, input().split())
    lst[p] = [c1, c2]

    if c1 != -1:
        parent[c1] = p
    if c2 != -1:
        parent[c2] = p

# level_min_max[i]: 레벨이 i일 때의 가장 왼쪽/오른쪽 노드 위치
level_min_max = [[21e8, -1] for _ in range(N + 1)]

idx = 0
def dfs(level, now):
    global idx

    if lst[now][0] != -1:
        dfs(level + 1, lst[now][0])
        
    idx += 1
    level_min_max[level][0] = min(level_min_max[level][0], idx)
    level_min_max[level][1] = max(level_min_max[level][1], idx)

    if lst[now][1] != -1:
        dfs(level + 1, lst[now][1])

for i in range(1, N + 1):
    if not parent[i]:
        dfs(1, i)
        break

result_width = 0
result_level = N + 1

for n in range(1, N + 1):
    width = level_min_max[n][1] - level_min_max[n][0] + 1
    if result_width < width:
        result_width = width
        result_level = n

print(result_level, result_width)