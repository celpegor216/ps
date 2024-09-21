N, K = map(int, input().split())

MAX = 21e8
lst = [[MAX] * N for _ in range(N)]

for i in range(N):
    lst[i][i] = 0

for _ in range(K):
    a, b = map(lambda x: int(x) - 1, input().split())
    lst[a][b] = 1
    lst[b][a] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

def check():
    for i in range(N):
        for j in range(i + 1, N):
            if lst[i][j] > 6:
                return 'Big World!'
    
    return 'Small World!'

print(check())