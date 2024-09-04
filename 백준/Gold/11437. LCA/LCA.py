# 반례 참고
# dfs가 메모리를 많이 먹어서 메모리초과였나?


from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

lst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

# parents[i][j]: i에서 2 ** j번 거슬러 올라간 부모노드
MAX = 16    # 2 * 16 = 65536
parents = [[0] * MAX for _ in range(N + 1)]
# 루트는 1번
parents[1][0] = -1
levels = [0] * (N + 1)

q = deque()
q.append(1)

while q:
    now = q.popleft()
    for nxt in lst[now]:
        if not parents[nxt][0]:
            parents[nxt][0] = now
            levels[nxt] = levels[now] + 1
            q.append(nxt)

# parent 테이블을 채울 때,
# 낮은 높이에 대해 모든 정점의 낮은 높이 부모를 찾고,
# 그 다음 높이로 건너가야 합니다.
parents[1][0] = 0
for i in sorted([x for x in range(2, N + 1)], key=lambda x: levels[x]):
    for j in range(1, MAX):
        parents[i][j] = parents[parents[i][j - 1]][j - 1]
        if not parents[i][j]:
            break

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    # a의 레벨이 더 크게
    if levels[a] < levels[b]:
        a, b = b, a

    # a가 b와 레벨이 같아지도록 끌어 올리기
    if levels[a] != levels[b]:
        for j in range(MAX - 1, -1, -1):
            if levels[a] - 2 ** j >= levels[b]:
                a = parents[a][j]
            if levels[a] == levels[b]:
                break

    # 공통 조상 찾기
    if a == b:
        print(a)
    else:
        for j in range(MAX - 1, -1, -1):
            if parents[a][j] != parents[b][j]:
                a = parents[a][j]
                b = parents[b][j]
        print(parents[a][0])