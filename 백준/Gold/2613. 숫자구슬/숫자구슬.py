# 반례 참고함, 이분 탐색으로 풀 수 없군...


N, M = map(int, input().split())
lst = list(map(int, input().split()))

# memo[i][j]: i부터 j까지 더한 값
memo = [[0] * N for _ in range(N)]

for i in range(N):
    memo[i][i] = lst[i]
    for j in range(i + 1, N):
        memo[i][j] = memo[i][j - 1] + lst[j]

used = [[[] for _ in range(M)] for _ in range(N)]

def dfs(level, start):
    global cnt_0, cnt_1

    if used[start][level]:
        return used[start][level]

    if level == M - 1:
        used[start][level] = [[N - 1], memo[start][N - 1]]
    else:
        min_max = 21e8
        group = []
        for i in range(start, N - 1):
            tmp_group, tmp_min_max = dfs(level + 1, i + 1)
            tmp_min_max = max(memo[start][i], tmp_min_max)

            if tmp_min_max < min_max:
                min_max = tmp_min_max
                group = [i] + tmp_group
        used[start][level] = [group, min_max]
    return used[start][level]

group, min_max = dfs(0, 0)

print(min_max)
group = [-1] + group
for m in range(M):
    print(group[m + 1] - group[m], end=' ')