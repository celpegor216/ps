N, X, Y = map(int, input().split())

result = set()

def dfs(level, now):
    global result, prefixed

    if level == N + 1:
        result.add(''.join([str(item) for item in now]))
        return
    
    if level == prefixed:
        dfs(level + 1, now)
    else:
        for n in range(1, N * 2):
            if n + level + 1 > N * 2:
                break

            if not now[n] and not now[n + level + 1]:
                tmp = now[:]
                tmp[n] = tmp[n + level + 1] = level
                dfs(level + 1, tmp)

prefixed = Y - X - 1
now = [0] * (N * 2 + 1)
now[X] = now[Y] = prefixed
dfs(1, now)

print(len(result))