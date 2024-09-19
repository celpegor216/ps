# N×M
N, M = map(int, input().split())
# 0은 바다, 1은 땅
lst = [list(map(int, input().split())) for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 섬 구분짓기
island = [[-1] * M for _ in range(N)]
island_cnt = 0
for i in range(N):
    for j in range(M):
        if island[i][j] != -1 or not lst[i][j]:
            continue

        q = []
        q.append((i, j))

        island[i][j] = island_cnt
        idx = 0
        while idx < len(q):
            y, x = q[idx]

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and island[ny][nx] == -1 and lst[ny][nx]:
                    island[ny][nx] = island_cnt
                    q.append((ny, nx))

            idx += 1

        island_cnt += 1

# island_to_island[i][j]: i 섬에서 j 섬까지 최단 직선 거리
# 다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안된다
# 다리의 길이는 2 이상이어야 한다
# 방향이 가로인 다리는 다리의 양 끝이 가로 방향으로 섬과 인접해야 하고,
# 방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접해야 한다.
# 섬 A와 B를 연결하는 다리가 중간에 섬 C와 인접한 바다를 지나가는 경우에 섬 C는 A, B와 연결되어있는 것이 아니다.
# 다리가 교차하는 경우가 있을 수도 있다.
# 교차하는 다리의 길이를 계산할 때는 각 칸이 각 다리의 길이에 모두 포함되어야 한다
MAX = 21e8
island_to_island = [[MAX] * island_cnt for _ in range(island_cnt)]

used = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if used[i][j] or island[i][j] == -1:
            continue

        q = []
        q.append((i, j))
        used[i][j] = 1

        now = island[i][j]

        idx = 0
        while idx < len(q):
            y, x = q[idx]

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx]:
                    if island[ny][nx] == now:
                        q.append((ny, nx))
                        used[ny][nx] = 1
                    else:
                        # 지금 방향으로 쭉 뻗어나가보기
                        nxt = -1
                        cnt = 0
                        while 0 <= ny < N and 0 <= nx < M:
                            if island[ny][nx] != -1 and lst[ny][nx] != now:
                                nxt = island[ny][nx]
                                break
                            ny += dy
                            nx += dx
                            cnt += 1

                        if nxt != -1 and cnt > 1 and island_to_island[now][nxt] > cnt:
                            island_to_island[now][nxt] = cnt
                            island_to_island[nxt][now] = cnt

            idx += 1


def find(a, groups):
    if groups[a] != a:
        groups[a] = find(groups[a], groups)
    return groups[a]

def union(a, b, groups):
    group_a, group_b = find(a, groups), find(b, groups)

    if group_a > group_b:
        group_a, group_b = group_b, group_a

    groups[group_b] = group_a


possible_edges = []
for i in range(island_cnt):
    for j in range(i + 1, island_cnt):
        if island_to_island[i][j] != MAX:
            possible_edges.append((i, j, island_to_island[i][j]))
edges_cnt = len(possible_edges)


# 모든 섬을 연결하는 다리 길이의 최솟값
# 모든 섬을 연결하는 것이 불가능하면 -1을 출력
result = MAX
def dfs(level, start, edges):
    global result

    # 다리는 섬 개수 - 1 개만 있으면 됨
    if level == island_cnt - 1:
        # 모든 섬이 연결된다면 정답 갱신
        groups = [n for n in range(island_cnt)]
        total = 0

        for i in edges:
            a, b, c = possible_edges[i]
            total += c
            union(a, b, groups)

        standard = groups[0]
        for i in range(1, island_cnt):
            if find(groups[i], groups) != standard:
                break
        else:
            result = min(result, total)
        return

    # 어떤 섬과 어떤 섬을 연결할 것인지 dfs로 정하기
    for i in range(start, edges_cnt):
        dfs(level + 1, i + 1, edges + [i])


dfs(0, 0, [])
print(result if result != MAX else -1)