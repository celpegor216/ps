from collections import deque

N, K = map(int, input().split())
lst = list(map(int, input().split()))

q = deque()
used = dict()
for item in lst:
    q.append((item, 0))
    used[item] = 1

result = 0
cnt = 0

while q:
    nowp, nowc = q.popleft()

    left, right = nowp - 1, nowp + 1
    if not used.get(left):
        result += nowc + 1
        cnt += 1
        q.append((left, nowc + 1))
        used[left] = 1
    
    if cnt == K:
        break

    if not used.get(right):
        result += nowc + 1
        cnt += 1
        q.append((right, nowc + 1))
        used[right] = 1

    if cnt == K:
        break

print(result)