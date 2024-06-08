import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
lst = [[10 ** 6 + 1] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().strip().split())
    a -= 1
    b -= 1
    lst[a][b] = min(lst[a][b], c)

path = [[-1] * N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if lst[i][j] > lst[i][k] + lst[k][j]:
                lst[i][j] = lst[i][k] + lst[k][j]
                path[i][j] = k

for n in range(N):
    lst[n][n] = 10 ** 6 + 1

for i in range(N):
    for j in range(N):
        if lst[i][j] == 10 ** 6 + 1:
            print(0, end = ' ')
        else:
            print(lst[i][j], end = ' ')
    print()

def find(start, end):
    if path[start][end] == -1:
        return [end + 1]

    return find(start, path[start][end]) + find(path[start][end], end)

for i in range(N):
    for j in range(N):
        if lst[i][j] == 10 ** 6 + 1:
            print(0)
        else:
            tmp = [i + 1] + find(i, j)
            print(len(tmp), *tmp)