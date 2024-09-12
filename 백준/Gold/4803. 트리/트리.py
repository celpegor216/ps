from collections import deque


tc = 0
while 1:
    tc += 1

    N, M = map(int, input().split())

    if N == M == 0:
        break

    lst = [[] for _ in range(N + 1)]

    for m in range(M):
        a, b = map(int, input().split())
        lst[a].append((m, b))
        lst[b].append((m, a))

    result = 0
    used = [0] * (N + 1)
    used_edges = [0] * (M + 1)
    for n in range(1, N + 1):
        if used[n]:
            continue

        q = deque()
        q.append(n)

        used[n] = 1

        is_tree = 1
        while q:
            now = q.popleft()

            for next_edge, next_node in lst[now]:
                if used_edges[next_edge]:
                   continue

                used_edges[next_edge] = 1

                if used[next_node]:
                    is_tree = 0

                used[next_node] = 1

                q.append(next_node)

        result += is_tree

    if not result:
        result = "No trees."
    elif result == 1:
        result = "There is one tree."
    else:
        result = f"A forest of {result} trees."

    print(f'Case {tc}: {result}')