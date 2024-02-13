# 시간 초과
# 해답: https://ji-gwang.tistory.com/481

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

used_down = [1] * (2 * N + 1)    # y - x => N ~ -N
used_up = [1] * (2 * N + 1)    # y + x => 0 ~ 2 * N

def dfs(y, x, cnt):
    global result

    if N % 2:
        if x == N:
            y += 1
            x = 0
        elif x == N + 1:
            y += 1
            x = 1
    else:
        if x == N:
            y += 1
            x = 1
        elif x == N + 1:
            y += 1
            x = 0

    if y == N:
        result = max(result, cnt)
        return
    
    if lst[y][x] and used_down[y - x + N] and used_up[y + x]:
        used_down[y - x + N] = 0
        used_up[y + x] = 0
        dfs(y, x + 2, cnt + 1)
        used_down[y - x + N] = 1
        used_up[y + x] = 1
    dfs(y, x + 2, cnt)

result = 0
dfs(0, 0, 0)
black = result

result = 0
dfs(0, 1, 0)
white = result

print(black + white)