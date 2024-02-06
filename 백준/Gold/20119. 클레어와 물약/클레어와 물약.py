# 힌트: 한 물약의 레시피가 여러 개일 수 있음
# 해답: https://welog.tistory.com/256

from collections import deque

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
recipes = [list(map(int, input().split())) for _ in range(M)]
L = int(input())
have = set(map(int, input().split()))

children = dict()

for m in range(M):
    if recipes[m][-1] not in have:
        for p in recipes[m][1:-1]:
            children[p] = children.get(p, []) + [m]

q = deque(have)

while q:
    now = q.popleft()

    if children.get(now):
        for child in children[now]:
            recipes[child][0] -= 1

            if not recipes[child][0] and recipes[child][-1] not in have:
                have.add(recipes[child][-1])
                q.append(recipes[child][-1])

print(len(have))
print(*sorted(have))