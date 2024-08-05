from collections import deque

T = int(input())
K = 14    # 최대 노드가 10000개 이므로 최대 2 ** 13 까지 점프할 수 있음

for _ in range(T):
    N = int(input())

    # levels[n]: n번 노드의 깊이
    levels = [0] * (N + 1)

    # parents[n][i]: n번 노드의 2 ** i번째 조상, 점프를 위함
    parents = [[0] * K for _ in range(N + 1)]

    # children[n]: n번 노드의 자식들, 깊이 계산을 위함
    children = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        parent, child = map(int, input().split())
        parents[child][0] = parent
        children[parent].append(child)

    A, B = map(int, input().split())

    # 빠른 탐색을 위해 조상 정리
    root = -1
    for n in range(1, N + 1):
        if not parents[n][0]:
            root = n
            continue

        for i in range(1, K):
            if parents[parents[n][i - 1]][i - 1] == 0:
                break
            parents[n][i] = parents[parents[n][i - 1]][i - 1]

    # 깊이 계산
    q = deque()
    q.append(root)
    levels[root] = 1

    while q:
        now = q.popleft()

        for item in children[now]:
            q.append(item)
            levels[item] = levels[now] + 1

    # 찾아야 하는 두 노드의 레벨을 동일하게 만들기
    # 레벨이 작은 노드를 A로 놓고 B를 끌어올리기
    if levels[A] > levels[B]:
        A, B = B, A

    while levels[A] != levels[B]:
        for i in range(1, K):
            if levels[A] > levels[parents[B][i]]:
                B = parents[B][i - 1]
                break

    # 가장 가까운 공통 조상 찾기
    while parents[A][0] != parents[B][0]:
        for i in range(K - 1, -1, -1):
            if parents[A][i] != parents[B][i]:
                A = parents[A][i]
                B = parents[B][i]
                break

    print(A if A == B else parents[A][0])