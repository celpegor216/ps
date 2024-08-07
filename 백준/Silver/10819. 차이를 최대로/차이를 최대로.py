N = int(input())
lst = list(map(int, input().split()))

result = -1    # 절댓값을 다 더하므로 0보다 커질 수 밖에 없음 > 음수로 설정하면 무조건 갱신
used = [-1] * N    # 순열

def dfs(level):
    global result

    if level == N:
        total = 0
        for n in range(N - 1):
            total += abs(used[n] - used[n + 1])
        result = max(result, total)
        return

    for n in range(N):
        if used[n] == -1:
            used[n] = lst[level]
            dfs(level + 1)
            used[n] = -1

dfs(0)

print(result)