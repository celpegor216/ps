# 원소 하나씩 넣어보면서 들어갈 자리가 있으면 다음 원소 넣고 아니면 패스

N = int(input())
lst = sorted(map(int, input().split()))

result = -1

def dfs(level, next, path):
    global result

    if level == N:
        if result == -1 or path < result:
            result = path[:]
        return

    for i in range(next, N):
        for j in range(N * 2 - (2 + lst[i]) + 1):
            if path[j] == 21e8 and path[j + 1 + lst[i]] == 21e8:
                path[j], path[j + 1 + lst[i]] = lst[i], lst[i]
                dfs(level + 1, i + 1, path)
                path[j], path[j + 1 + lst[i]] = 21e8, 21e8

dfs(0, 0, [21e8] * N * 2)

if result == -1:
    print(result)
else:
    print(*result)