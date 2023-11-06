# 힌트: bfs, dfs
# 해답: https://hye-z.tistory.com/49

from collections import deque
import sys
input = sys.stdin.readline

K = int(input())

def bfs(num):
    global result

    q.append((num, 1))
    group[num] = 1

    while q:
        nown, nowg = q.popleft()

        used[nown] = 1

        for item in graph[nown]:
            if not group[item]:
                group[item] = -nowg
                q.append((item, -nowg))
            elif group[item] == nowg:
                result = 'NO'
                return
            elif not used[item]:
                q.append((item, group[item]))

for k in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    for e in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    group = [0] * (V + 1)
    used = [0] * (V + 1)

    result = 'YES'

    for v in range(1, V + 1):
        if not used[v]:
            bfs(v)
        
        if result == 'NO':
            break
    
    print(result)