N = int(input())
lst = [[]] + [list(map(int, input().split())) for _ in range(N - 1)] # 1칸 점프, 2칸 점프
K = int(input()) # 3칸 점프, 1번만 가능

result = 21e8
def dfs(level, total, used):
    global result

    if level == N:
        result = min(result, total)
        return
    
    dfs(level + 1, total + lst[level][0], used)
    
    if level + 2 <= N:
        dfs(level + 2, total + lst[level][1], used)
    
    if level + 3 <= N and not used:
        dfs(level + 3, total + K, True)

dfs(1, 0, False)

print(result)