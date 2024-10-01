N, K = input().split()
K = int(K)
M = len(N)

used = [set() for _ in range(K)]

def dfs(level, now):
    if level == K:
        return

    for i in range(M - 1):
        for j in range(i + 1, M):
            if i == 0 and now[j] == '0':
                continue

            nxt = now[:]
            nxt[i], nxt[j] = nxt[j], nxt[i]

            num = int(''.join(nxt))
            if num in used[level]:
                continue

            used[level].add(num)

            dfs(level + 1, nxt)


dfs(0, list(N))


if used[-1]:
    print(max(used[-1]))
else:
    print(-1)