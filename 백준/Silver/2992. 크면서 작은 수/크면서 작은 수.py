S = input()
sorted_S = sorted(S)
N = len(S)

result = 0
used = [0] * N
def dfs(level, now):
    global result

    if result:
        return

    if level == N:
        if now > S:
            result = now
        return

    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, now + sorted_S[i])
            used[i] = 0

dfs(0, '')

print(result)