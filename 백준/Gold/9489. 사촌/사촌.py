from collections import deque

while 1:
    N, K = map(int, input().split())

    if N == K == 0:
        break

    lst = list(map(int, input().split()))

    tree = dict()
    tree[lst[0]] = []
    parents = dict()
    parents[lst[0]] = -1
    q = deque()
    q.append(lst[0])

    for n in range(1, N):
        tree[q[0]].append(lst[n])
        tree[lst[n]] = []
        parents[lst[n]] = q[0]
        q.append(lst[n])

        if n < N - 1 and lst[n + 1] - lst[n] != 1:
            q.popleft()

    if parents[K] == -1 or parents[parents[K]] == -1:
        print(0)
        continue

    result = 0
    for child in tree[parents[parents[K]]]:
        if child == parents[K]:
            continue
        result += len(tree[child])

    print(result)