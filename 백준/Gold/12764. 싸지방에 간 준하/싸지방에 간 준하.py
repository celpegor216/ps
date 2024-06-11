import heapq

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()

q = []
used = [0] * (N + 1)
cnt = [0] * (N + 1)
result = 0

for s, e in lst:
    while q and q[0][0] < s:
        used[heapq.heappop(q)[1]] = 0

    for n in range(1, N + 1):
        if not used[n]:
            heapq.heappush(q, (e, n))
            used[n] = 1
            cnt[n] += 1
            break

    result = max(result, len(q))

print(result)

for n in range(1, N + 1):
    if not cnt[n]:
        break
    print(cnt[n], end=' ')