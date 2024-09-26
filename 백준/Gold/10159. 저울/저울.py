N = int(input())
M = int(input())
parent = [[] for _ in range(N + 1)]
children = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    children[a].append(b)
    parent[b].append(a)

for i in range(1, N + 1):
    used = [0] * (N + 1)
    used[i] = 1

    # 부모가 될 수 있는 것들 찾기
    q = [i]

    while q:
        nq = []

        for now in q:
            for p in parent[now]:
                if used[p]:
                    continue

                used[p] = 1
                nq.append(p)

        q = nq

    # 자식이 될 수 있는 것들 찾기
    q = [i]

    while q:
        nq = []

        for now in q:
            for c in children[now]:
                if used[c]:
                    continue

                used[c] = 1
                nq.append(c)

        q = nq

    print(used.count(0) - 1)