# 힌트: BFS
# 시간 초과가 풀리지 않음...
# 해답: https://tight-sleep.tistory.com/54

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

for line in lst:
    line.sort()

S, E = map(int, input().split())

prev = [0] * (N + 1)
used = [0] * (N + 1)

def S_to_E():
    prev[S] = S
    
    q = deque()
    q.append((S, 0))

    while q:
        now, cnt = q.popleft()

        if now == E:
            return cnt
        
        for num in lst[now]:
            if not prev[num]:
                prev[num] = now
                q.append((num, cnt + 1))

result = S_to_E()

now = E
while prev[now] != now:
    used[now] = 1
    now = prev[now]

q = deque()
q.append((E, 0))
used[E] = 1

while q:
    now, cnt = q.popleft()

    if now == S:
        result += cnt
        break

    for num in lst[now]:
        if not used[num]:
            used[num] = 1
            q.append((num, cnt + 1))

print(result)