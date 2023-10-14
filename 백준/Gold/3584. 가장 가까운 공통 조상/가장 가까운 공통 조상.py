from collections import deque

T = int(input())

for t in range(T):
    N = int(input())
    children = [[] for _ in range(N + 1)]
    parents = [[0] * 20 for _ in range(N + 1)]
    levels = [0] * (N + 1)

    for n in range(N - 1):
        A, B = map(int, input().split())
        children[A].append(B)
        parents[B][0] = A
    
    root = 0
    for n in range(1, N + 1):
        if parents[n][0] == 0:
            root = n
            break
    
    levels[root] = 1

    q = deque()
    q.append(root)

    while q:
        now = q.popleft()

        for item in children[now]:
            levels[item] = levels[now] + 1
            q.append(item)
    
    for i in range(1, 20):
        for j in range(1, N + 1):
            parents[j][i] = parents[parents[j][i - 1]][i - 1]
    
    A, B = map(int, input().split())

    if levels[A] < levels[B]:
        A, B = B, A
    
    # A 레벨을 높여서 B와 레벨 맞추기
    if levels[A] != levels[B]:
        for i in range(19, -1, -1):
            if levels[parents[A][i]] >= levels[B]:
                A = parents[A][i]
    
    result = A

    # A와 B의 공통 조상 찾기
    if A != B:
        for i in range(19, -1, -1):
            if parents[A][i] != parents[B][i]:
                A = parents[A][i]
                B = parents[B][i]
            
            result = parents[A][i]

    print(result)