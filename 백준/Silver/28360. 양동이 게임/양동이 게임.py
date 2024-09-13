N, M = map(int, input().split())
children = [[] for _ in range(N + 1)]

for _ in range(M):
    p, c = map(int, input().split())
    children[p].append(c)

used = [0] * (N + 1)
used[1] = 100

result = 0

for n in range(1, N + 1):
    water = used[n]
    length = len(children[n])

    if not length:
        result = max(result, water)
    else:
        nxt_water = water / length
        for child in children[n]:
            used[child] += nxt_water

print(result)