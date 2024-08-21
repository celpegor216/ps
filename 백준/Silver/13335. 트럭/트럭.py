from collections import deque

N, W, L = map(int, input().split())
lst = list(map(int, input().split()))

q = deque([0] * W)
l = 0

result = 0
for n in range(N):
    cnt = 0
    while q[-1] != 0 or l + lst[n] > L:
        l -= q.popleft()
        q.append(0)
        cnt += 1

    if cnt:
        result += cnt
    else:
        result += 1
    q[-1] = lst[n]
    l += lst[n]

last_idx = 0
for w in range(W):
    if q[w]:
        last_idx = w

print(result + last_idx + 1)