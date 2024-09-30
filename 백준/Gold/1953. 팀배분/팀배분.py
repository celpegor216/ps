N = int(input())
lst = [[]]
for _ in range(N):
    n, *tmp = map(int, input().split())
    lst.append(tmp)

used = [0] * (N + 1)

for i in range(1, N + 1):
    if used[i]:
        continue

    used[i] = 1
    q = [i]

    while q:
        nq = []

        for now in q:
            for nxt in lst[now]:
                if used[nxt]:
                    continue

                used[nxt] = -used[now]
                nq.append(nxt)

        q = nq


blue = []
white = []
for i in range(1, N + 1):
    if used[i] == 1:
        blue.append(i)
    else:
        white.append(i)

for team in (blue, white):
    print(len(team))
    print(*team)
