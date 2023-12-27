# 해답: https://hongcoding.tistory.com/95

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

children = [[] for _ in range(N + 1)]
level = [0] * (N + 1)

q = deque()
result = []

for m in range(M):
    parent, child = map(int, input().split())

    children[parent].append(child)
    level[child] += 1

for n in range(1, N + 1):
    if not level[n]:
        q.append(n)

while q:
    now = q.popleft()
    result.append(now)

    for child in children[now]:
        level[child] -= 1

        # 앞에 서야 하는 모든 부모가 섰을 때 자식을 세움
        if not level[child]:
            q.append(child)

print(*result)