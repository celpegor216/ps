from collections import deque

N = int(input())
lst = list(map(int, input().split()))
S = int(input()) - 1

q = deque()
q.append(S)

used = [0] * N
used[S] = 1

while q:
    now = q.popleft()

    left = now - lst[now]
    right = now + lst[now]

    if left >= 0 and not used[left]:
        q.append(left)
        used[left] = 1
    
    if right < N and not used[right]:
        q.append(right)
        used[right] = 1

print(sum(used))