N, K, Q, M = map(int, input().split())
sleeps = list(map(int, input().split()))
starts = list(map(int, input().split()))

used = [1] * (N + 3)

for start in starts:
    if start in sleeps:
        continue
    nxt = start
    while nxt <= N + 2:
        if nxt not in sleeps:
            used[nxt] = 0
        nxt += start

for n in range(1, N + 3):
    used[n] += used[n - 1]

for _ in range(M):
    s, e = map(int, input().split())
    print(used[e] - used[s - 1])