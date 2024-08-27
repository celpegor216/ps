from collections import deque

N, K = map(int, input().split())
S = input().replace(' ', '')
target = ''.join([str(x) for x in range(1, N + 1)])

used = set()
used.add(S)

q = deque()
q.append((S, 0))

result = -1
while q:
    now, cnt = q.popleft()

    if now == target:
        result = cnt
        break

    for i in range(N - K + 1):
        tmp = now[:i] + now[i:i + K][::-1] + now[i + K:]
        if tmp not in used:
            used.add(tmp)
            q.append((tmp, cnt + 1))

print(result)