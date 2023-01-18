# 시간초과 해결 방법: array[N-1][N-1]이 1인지 검사하는 코드를 추가

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 0

types = {0: [0, 2], 1: [1, 2], 2: [0, 1, 2]}

def dfs(y, x, nowt):
    global result
    
    if y == N - 1 and x == N - 1:
        result += 1
        return

    for t in types[nowt]:
        if t == 0 and x + 1 < N and lst[y][x + 1] != 1:
            dfs(y, x + 1, t)
        elif t == 1 and y + 1 < N and lst[y + 1][x] != 1:
            dfs(y + 1, x, t)
        elif t == 2 and x + 1 < N and y + 1 < N and lst[y][x + 1] != 1 and lst[y + 1][x] != 1 and lst[y + 1][x + 1] != 1:
            dfs(y + 1, x + 1, t)

if lst[-1][-1] == 1:
    print(0)
else:
    dfs(0, 1, 0)
    print(result)