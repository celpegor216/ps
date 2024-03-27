# dfs로 풀었을 때 시간초과
# 해답: https://recordofwonseok.tistory.com/370

N, M = map(int, input().split())
lst = [input() for _ in range(N)]
used = [[0] * M for _ in range(N)]

result = 0

# dfs를 그리디하게 탐색
# (n, 0)에서 시작해서 어떻게 가든 끝까지 가면 무조건 종료
def dfs(y, x):
    if x == M - 1:
        return True
    
    for dy in (-1, 0, 1):
        ny, nx = y + dy, x + 1
        if 0 <= ny < N and 0 <= nx < M:
            if lst[ny][nx] == '.' and not used[ny][nx]:
                used[ny][nx] = 1
                if dfs(ny, nx):
                    return True
    
    return False

for n in range(N):
    if dfs(n, 0):
        result += 1

print(result)