# 힌트: 트리의 지름은 아무 노드에서 bfs(dfs도 무관)를 통해 가정 멀리있는 노드를 구한 후 해당 노드에서 bfs를 한번더 진행하여 가장 멀리있는 노드를 구하면 된다
# 해답: https://velog.io/@coding_egg/%EB%B0%B1%EC%A4%80-1991%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%80%EB%A6%84-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V + 1)]

for v in range(V):
    temp = list(map(int, input().split()))

    for i in range(1, len(temp) - 1, 2):
        tree[temp[0]].append([temp[i], temp[i + 1]])

def bfs(start):
    q = deque()
    q.append(start)

    used = [-1] * (V + 1)
    used[start] = 0

    while q:
        nowv = q.popleft()

        for nextv, nextw in tree[nowv]:
            if used[nextv] == -1:
                q.append(nextv)
                used[nextv] = used[nowv] + nextw

    maxw = max(used)

    return used.index(maxw), maxw

start, cost = bfs(1)
end, cost = bfs(start)

print(cost)