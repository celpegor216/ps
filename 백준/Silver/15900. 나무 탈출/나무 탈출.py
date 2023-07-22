# 간선이 위에서부터 주어지지 않는다면 어떻게 트리를 그려야하지?

import sys
sys.setrecursionlimit(600000)

N = int(input())
dic = dict()

for n in range(N - 1):
    a, b = map(int, input().split())
    
    if dic.get(a):
        dic[a].append(b)
    else:
        dic[a] = [b]
    
    if dic.get(b):
        dic[b].append(a)
    else:
        dic[b] = [a]

total = 0
def dfs(level, parent, now):
    global total

    if now != 1 and len(dic[now]) == 1:
        total += level
        return

    for item in dic[now]:
        if item == parent: continue
        dfs(level + 1, now, item)

dfs(0, 0, 1)

if not total % 2:
    print('No')
else:
    print('Yes')