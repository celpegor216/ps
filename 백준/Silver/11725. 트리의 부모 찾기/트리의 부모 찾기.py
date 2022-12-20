# 힌트: 위 소스코드는 입력받은 순서에 의존합니다.
# N <= 100,000 이므로 dfs 사용하면 재귀 깊이 에러 발생

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
tree[1] = [1]

used = [0] * (N + 1)

for n in range(N - 1):
    a, b = map(int, input().split())

    tree[a].append(b)
    tree[b].append(a)

def bfs(num):
    q = deque()
    q.append(num)

    while q:
        nown = q.popleft()

        for item in tree[nown]:
            if not used[item]:
                used[item] = nown
                q.append(item)

bfs(1)

for i in range(2, len(used)):
    print(used[i])