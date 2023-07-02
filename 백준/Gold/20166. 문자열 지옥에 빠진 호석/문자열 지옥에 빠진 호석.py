N, M, K = map(int, input().split())
lst = [input() for _ in range(N)]

dic = dict()

def dfs(level, y, x, path):
    if path in dic.keys():
        dic[path] += 1
    else:
        dic[path] = 1

    if level == 5:
        return
    
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        ny, nx = (y + dy) % N, (x + dx) % M
        dfs(level + 1, ny, nx, path + lst[ny][nx])

for n in range(N):
    for m in range(M):
        dfs(1, n, m, lst[n][m])

for k in range(K):
    key = input()
    result = dic.get(key)

    if not result:
        print(0)
    else:
        print(result)