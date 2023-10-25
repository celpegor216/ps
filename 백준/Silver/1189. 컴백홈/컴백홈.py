N, M, K = map(int, input().split())
lst = [input() for _ in range(N)]

result = 0
used = [[0] * M for _ in range(N)]

def dfs(y, x, total):
    global result

    if y == 0 and x == M - 1:
        if total == K:
            result += 1
        return
    
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] != 'T':
            used[ny][nx] = 1
            dfs(ny, nx, total + 1)
            used[ny][nx] = 0

used[N - 1][0] = 1
dfs(N - 1, 0, 1)

print(result)