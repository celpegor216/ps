# 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이
# 해답: https://fre2-dom.tistory.com/232

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

N = int(input())
tree = [[] for _ in range(N + 1)]

for n in range(N - 1):
    parent, child, weight = map(int, input().split())

    tree[parent].append([child, weight])
    tree[child].append([parent, weight])


def dfs(start, total):
    for item in tree[start]:
        if used[item[0]] == -1:
            used[item[0]] = total + item[1]
            dfs(item[0], total + item[1])

# 루트 노드에서 가장 멀리 떨어진 노드 구하기
used = [-1] * (N + 1)
used[1] = 0
dfs(1, 0)

# 앞에서 구한 노드에서 가장 멀리 떨어진 노드 구하기
start = used.index(max(used))
used = [-1] * (N + 1)
used[start] = 0
dfs(start, 0)

print(max(used))