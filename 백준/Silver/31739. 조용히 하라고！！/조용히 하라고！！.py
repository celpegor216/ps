N, M, K, T, P = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]

result_A = result_B = 0

# 우정이는 0~T초 사이에 모든 모기를 잡음
used = [0] * K
def dfs(before, time, total):
    global result_A

    if time > T:
        return

    result_A = max(result_A, total)

    for k in range(K):
        if not used[k]:
            used[k] = 1
            dfs(k, abs(lst[before][0] - lst[k][0]) + abs(lst[before][1] - lst[k][1]) + time, total + 1)
            used[k] = 0

for k in range(K):
    used[k] = 1
    dfs(k, 0, 1)
    used[k] = 0

# 우정이는 특정 좌표에 전기장을 형성해서 모기를 잡음
for n in range(1, N + 1):
    for m in range(1, M + 1):
        total = 0

        for i in range(K):
            L = abs(lst[i][0] - n) + abs(lst[i][1] - m)
            if L == 0 or lst[i][2] <= P / L:
                total += 1

        result_B = max(result_B, total)

print(result_A, result_B)