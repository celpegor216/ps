from collections import deque

N, M = map(int, input().split())
# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
lst = [list(map(int, input().split())) for _ in range(N)]
blanks = []
virus = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            blanks.append((i, j))
        elif lst[i][j] == 2:
            virus.append((i, j))

MAX = len(blanks)

# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다
result = 0
def dfs(level, start):
    global result

    # 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역
    if level == 3:
        # bfs
        q = deque(virus)
        used = [[0] * M for _ in range(N)]

        while q:
            y, x = q.popleft()

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and not lst[ny][nx] :
                    used[ny][nx] = 1
                    q.append((ny, nx))

        total = 0
        for i in range(N):
            for j in range(M):
                if not used[i][j] and not lst[i][j]:
                    total += 1

        result = max(result, total)
        return

    for idx in range(start, MAX):
        y, x = blanks[idx]
        if not lst[y][x]:
            lst[y][x] = 1
            dfs(level + 1, idx + 1)
            lst[y][x] = 0

dfs(0, 0)

# 얻을 수 있는 안전 영역 크기의 최댓값
print(result)