import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

N = int(input())
lst = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

level = [0] * (N + 1)
parent = [[0] * 20 for _ in range(N + 1)]

def make_tree(now, l):
    level[now] = l

    for i in range(1, 20):
        if parent[parent[now][i - 1]][i - 1] == 0:
            break

        parent[now][i] = parent[parent[now][i - 1]][i - 1]

    for item in lst[now]:
        if not level[item]:
            parent[item][0] = now
            make_tree(item, l + 1)

make_tree(1, 1)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())

    # level 맞추기
    if level[a] != level[b]:
        if level[a] < level[b]:
            a, b = b, a
        
        while level[a] != level[b]:
            for i in range(20):
                if level[parent[a][i]] < level[b]:
                    a = parent[a][i - 1]
                    break
    
    # 공통 조상 찾기
    while a != b:
        a, b = parent[a][0], parent[b][0]
        
    print(a)