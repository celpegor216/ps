N = int(input())

used = [0] * N    # 1부터 N까지의 수로 이루어진 순열

def dfs(level, now):
    if level == N:
        print(*now)
        return

    for i in range(N):    # 사전순
        if not used[i]:
            used[i] = 1
            dfs(level + 1, now + [i + 1])
            used[i] = 0

dfs(0, [])