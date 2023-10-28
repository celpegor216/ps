# 힌트: BFS + 이분 탐색

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [dict() for _ in range(N + 1)]

for m in range(M):
    A, B, C = map(int, input().split())

    if not lst[A].get(B) or (lst[A].get(B) and C > lst[A][B]):
        lst[A][B] = C
        lst[B][A] = C

S, E = map(int, input().split())

start, end = 1, 10 ** 9
result = 0

while start <= end:
    middle = (start + end) // 2
    tmp = 0

    used = [0] * (N + 1)
    q = deque()

    used[S] = 1
    q.append(S)

    while q:
        now = q.popleft()

        if now == E:
            tmp = 1
            break

        for k, v in lst[now].items():
            if not used[k] and v >= middle:
                used[k] = 1
                q.append(k)
    
    if tmp:
        result = max(result, middle)
        start = middle + 1
    else:
        end = middle - 1

print(result)