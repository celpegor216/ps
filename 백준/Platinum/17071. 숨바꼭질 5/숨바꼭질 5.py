from collections import deque


N, K = map(int, input().split())

MAX = 500000
# used[0][i]: i에 짝수번째 횟수로 도착했을 때의 최소 횟수
# used[1][i]: i에 홀수번째 횟수로 도착했을 때의 최소 횟수
used = [[MAX + 1] * (MAX + 1) for _ in range(2)]

q = deque()
q.append(N)

used[0][N] = 0

result = -1
k = 0
while K <= MAX:
    if used[k % 2][K] != MAX + 1:
        result = k
        break

    if K - 1 >= 0 and used[(k + 1) % 2][K - 1] != MAX + 1:
        result = k
        break

    if K + 1 <= MAX and used[(k + 1) % 2][K + 1] != MAX + 1:
        result = K
        break

    if K > 0 and not K % 2 and used[(k + 1) % 2][K // 2] != MAX + 1:
        result = k
        break

    k += 1
    K += k
    for _ in range(len(q)):
        now = q.popleft()

        for nxt in (now + 1, now - 1, now * 2):
            if not (0 <= nxt <= MAX):
                continue

            if used[k % 2][nxt] <= k:
                continue

            used[k % 2][nxt] = k
            q.append(nxt)


print(result)