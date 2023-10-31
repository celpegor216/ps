# 힌트: https://www.acmicpc.net/board/view/91635

N = int(input())
lst = list(map(int, input().split()))
calcs = list(map(int, input().split())) # +, -, *, //

maxv = -1000000000
minv = 1000000000

def dfs(level, total):
    global maxv, minv

    if level == N:
        maxv = max(maxv, total)
        minv = min(minv, total)
        return
    
    for i in range(4):
        if calcs[i]:
            calcs[i] -= 1

            if i == 0:
                dfs(level + 1, total + lst[level])
            elif i == 1:
                dfs(level + 1, total - lst[level])
            elif i == 2:
                dfs(level + 1, total * lst[level])
            elif i == 3:
                dfs(level + 1, int(total / lst[level]))

            calcs[i] += 1

dfs(1, lst[0])

print(maxv)
print(minv)