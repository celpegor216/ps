# 만들 수 있는 모든 매직 스퀘어 배열을 만들어두기
# 각각의 행/열/대각선 총합이 15여야 함
N = 3
sqr_N = N ** 2
TARGET = 15

squares = []

used = [0] * sqr_N
def dfs(level, now):
    if level == sqr_N:
        squares.append([line[:] for line in now])
        return
    
    for i in range(sqr_N):
        if used[i]:
            continue

        nxt = [line[:] for line in now]
        y, x = level // N, level % N
        nxt[y][x] = i + 1

        # 가로 체크
        if x == 2 and sum(nxt[y]) != TARGET:
            continue

        # 세로 체크
        if y == 2 and sum([nxt[n][x] for n in range(N)]) != TARGET:
            continue

        # 대각선 체크
        if y == 2 and x == 0 and (nxt[2][0] + nxt[1][1] + nxt[0][2]) != TARGET:
            continue

        if y == x == 2 and (nxt[0][0] + nxt[1][1] + nxt[2][2]) != TARGET:
            continue
        
        used[i] = 1
        dfs(level + 1, nxt)
        used[i] = 0

dfs(0, [[0] * N for _ in range(N)])


lst = [list(map(int, input().split())) for _ in range(N)]

result = sqr_N * 9
for square in squares:
    total = 0
    for i in range(N):
        for j in range(N):
            total += abs(square[i][j] - lst[i][j])
    result = min(result, total)

print(result)