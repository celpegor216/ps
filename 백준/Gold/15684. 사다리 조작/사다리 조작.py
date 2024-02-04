N, M, H = map(int, input().split())
lines = [[0] * (N + 1) for _ in range(H + 1)]

for m in range(M):
    h, n = map(int, input().split())
    lines[h][n] = 1

result = 4

def dfs(start, nown, nowh, cnt):
    global result

    if cnt >= result:
        return
    
    if nowh == H + 1:
        if start == nown == N:
            result = min(result, cnt)
        elif start == nown:
            dfs(start + 1, start + 1, 1, cnt)
        return
    
    left = nown - 1
    right = nown

    if 0 < left and lines[nowh][left]:
        dfs(start, left, nowh + 1, cnt)
    elif lines[nowh][right]:
        dfs(start, right + 1, nowh + 1, cnt)
    else:
        dfs(start, nown, nowh + 1, cnt)

        if (0 == left - 1) or (0 < left - 1 and not lines[nowh][left - 1]):
            lines[nowh][left] = 1
            dfs(start, left, nowh + 1, cnt + 1)
            lines[nowh][left] = 0
        
        if (right + 1 == N) or (right + 1 < N and not lines[nowh][right + 1]):
            lines[nowh][right] = 1
            dfs(start, right + 1, nowh + 1, cnt + 1)
            lines[nowh][right] = 0
        
dfs(1, 1, 1, 0)

print(result if result < 4 else -1)