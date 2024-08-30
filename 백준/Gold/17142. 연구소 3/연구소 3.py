from collections import deque

N, H = map(int, input().split())
# 크기가 N×N
M = N
# 0은 빈 칸, 1은 벽, 2는 비활성 바이러스
lst = [list(map(int, input().split())) for _ in range(N)]

not_activated = []
blank_cnt = 0    # 병원과 벽을 제외한 모든 지역에 바이러스
for i in range(N):
    for j in range(M):
        if lst[i][j] == 2:
            not_activated.append((i, j))
        elif lst[i][j] == 0:
            blank_cnt += 1
length = len(not_activated)

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# H가 최대 10이므로 dfs로 조합 만들어서 bfs 돌리면 되겠다
selected = [0] * length
# 활성 바이러스가 하나만 있을 때 전체에 퍼지기 위해 필요한 가장 긴 시간(대충)
MAX = N * M
# 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간
result = MAX
def dfs(level, start):
    global result

    # H개의 비활성 바이러스를 적절히 골라
    if level == H:
        # bfs
        # 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제
        q = deque()
        used = [[0] * M for _ in range(N)]
        left_blank_cnt = blank_cnt

        for i in range(length):
            if selected[i]:
                q.append(not_activated[i])
                used[not_activated[i][0]][not_activated[i][1]] = 1

        time = 0
        while left_blank_cnt and q:
            time += 1
            for _ in range(len(q)):
                y, x = q.popleft()
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == 1:
                        continue

                    if used[ny][nx]:
                        continue

                    used[ny][nx] = 1
                    q.append((ny, nx))

                    if lst[ny][nx] == 0:
                        left_blank_cnt -= 1

        if not left_blank_cnt:
            result = min(result, time)

        return

    for i in range(start, length):
        if not selected[i]:
            selected[i] = 1
            dfs(level + 1, i + 1)
            selected[i] = 0

dfs(0, 0)

# 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1
print(result if result != MAX else -1)
