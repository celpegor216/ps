N = int(input())
lst = [input().split() for _ in range(N)]

maxv = -21e8
minv = 21e8

def dfs(y, x, path):
    global maxv, minv

    if y == N - 1 and x == N - 1:
        nowv = int(path[0])

        for n in range(1, N):
            calc = path[2 * n - 1]
            num = int(path[2 * n])
            
            if calc == '+':
                nowv += num
            elif calc == '-':
                nowv -= num
            elif calc == '*':
                nowv *= num

        maxv = max(maxv, nowv)
        minv = min(minv, nowv)
        return

    for ny, nx in ((y, x + 1), (y + 1, x)):
        if 0 <= ny < N and 0 <= nx < N:
            dfs(ny, nx, path + [lst[ny][nx]])

dfs(0, 0, [lst[0][0]])

print(maxv, minv)