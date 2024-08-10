from collections import deque
import sys
input = sys.stdin.readline

N, S, D = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

# 위상정렬을 사용하기 위해 부모와 자식의 수 파악해서 트리 구조화
# 이때 루트는 시작점 S
parents_idx = [-1] * (N + 1)
children_cnt = [0] * (N + 1)

q = deque()
q.append(S)
parents_idx[S] = 0

while q:
    now = q.popleft()

    for child in lst[now]:
        if parents_idx[child] == -1:
            parents_idx[child] = now
            children_cnt[now] += 1
            q.append(child)

# 리프 노드로부터 D만큼 떨어진 노드들을 제외시킴
used = [0] * (N + 1)
q = deque()
for i in range(1, N + 1):
    if not children_cnt[i]:
        q.append(i)
        used[i] = 1

while q:
    now = q.popleft()

    parent = parents_idx[now]
    children_cnt[parent] -= 1

    if children_cnt[parent] == 0:
        used[parent] = used[now] + 1
        q.append(parent)

result = 0

for i in range(1, N + 1):
    if used[i] > D:
        result += 1

print((result - 1) * 2 if result else 0)