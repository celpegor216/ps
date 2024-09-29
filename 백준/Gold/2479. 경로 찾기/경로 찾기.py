N, K = map(int, input().split())
codes = [input() for _ in range(N)]
A, B = map(lambda x: int(x) - 1, input().split())

lst = [[] for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        dist = 0
        for k in range(K):
            if codes[i][k] != codes[j][k]:
                dist += 1
        if dist == 1:
            lst[i].append(j)
            lst[j].append(i)


def find():
    q = [A]
    parent = [-1] * N
    parent[A] = -2

    while q:
        nq = []

        for now in q:
            if now == B:
                path = []
                while now != -2:
                    path.append(now + 1)
                    now = parent[now]
                return path[::-1]


            for nxt in lst[now]:
                if parent[nxt] != -1:
                    continue
                
                parent[nxt] = now
                nq.append(nxt)
        
        q = nq
    
    return [-1]


print(*find())