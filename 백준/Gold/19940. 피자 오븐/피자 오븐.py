T = int(input())

times = [60, 10, -10, 1, -1]

q = []
memo = [[] for _ in range(61)]
memo[0] = [0] * 5

for i in (0, 1, 3):
    now = times[i]
    memo[now] = [0] * 5
    memo[now][i] += 1
    q.append((now, memo[now]))

while q:
    nq = []

    for time, path in q:
        for i in range(5):
            nxt = time + times[i]
            nxt_path = path[:]
            nxt_path[i] += 1
            if not (0 <= nxt <= 60):
                continue

            if memo[nxt] and (sum(memo[nxt]) < sum(nxt_path) or (sum(memo[nxt]) == sum(nxt_path) and memo[nxt] <= nxt_path)):
                continue
            memo[nxt] = nxt_path
            nq.append((nxt, memo[nxt]))

    q = nq


for _ in range(T):
    N = int(input())

    result = memo[N % 60][:]
    result[0] += N // 60

    print(*result)
