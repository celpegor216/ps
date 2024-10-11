# 반례 참고


N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

# 오른쪽 아래로 갈 수 있는 칸의 수
# 왼쪽 아래로 갈 수 있는 칸의 수
possibles = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# 오른쪽 아래 탐색
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if not lst[i][j] or possibles[i][j][0]:
            continue

        cnt = 1
        possibles[i][j][0] = 1
        ny, nx = i - 1, j - 1
        while 0 <= ny < N and 0 <= nx < M and lst[ny][nx]:
            cnt += 1
            possibles[ny][nx][0] = cnt
            ny -= 1
            nx -= 1

# 왼쪽 아래 탐색
for i in range(N - 1, -1, -1):
    for j in range(M):
        if not lst[i][j] or possibles[i][j][1]:
            continue

        cnt = 1
        possibles[i][j][1] = 1
        ny, nx = i - 1, j + 1
        while 0 <= ny < N and 0 <= nx < M and lst[ny][nx]:
            cnt += 1
            possibles[ny][nx][1] = cnt
            ny -= 1
            nx += 1

result = 0
for i in range(N):
    for j in range(M):
        if not lst[i][j]:
            continue

        size = min(*possibles[i][j], j + 1, M - j)

        for s in range(size, 0, -1):
            if possibles[i + (s - 1)][j - (s - 1)][0] >= s and possibles[i + (s - 1)][j + (s - 1)][1] >= s:
                result = max(result, s)
                break

print(result)