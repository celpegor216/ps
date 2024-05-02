import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

parents = [[0] * 20 for _ in range(N + 1)]
levels = [0] * (N + 1)

def make_graph(now, level, parent):
    levels[now] = level

    parents[now][0] = parent
    for i in range(1, 20):
        if parent == 0:
            break
        
        parent = parents[parent][i - 1]
        parents[now][i] = parent

    for item in graph[now]:
        if not levels[item]:
            make_graph(item, level + 1, now)

make_graph(1, 1, 0)

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())

    # b를 a보다 level이 작거나 같은 것으로 설정하고 level 맞추기
    if levels[a] < levels[b]:
        a, b = b, a
    
    for i in range(19, -1, -1):
        if levels[a] == levels[b]:
            break

        if levels[parents[a][i]] >= levels[b]:
            a = parents[a][i]

    # 공통 조상 찾기
    if a != b:
        for i in range(19, -1, -1):
            if parents[a][i] != parents[b][i]:
                a = parents[a][i]
                b = parents[b][i]
        a = parents[a][0]

    print(a)