# 힌트: https://sorryhyeon.tistory.com/72
# input 변경으로 시간 초과 해결 시도
# 20번 라인 group[y]가 아닌 group[y_group]
# 43번 라인 group[u]가 아닌 find(u)

import sys
input = sys.stdin.readline

T = int(input())

def find(x):
    if x == group[x]:
        return x
    group[x] = find(group[x])
    return group[x]

def union(x, y):
    x_group, y_group = find(x), find(y)

    if x_group != y_group:
        group[y_group] = x_group

for t in range(T):
    N = int(input())
    group = [x for x in range(N)]

    K = int(input())

    for k in range(K):
        a, b = map(int, input().split())

        if a > b:
            a, b = b, a

        union(a, b)
    
    M = int(input())

    print(f'Scenario {t + 1}:')
    for m in range(M):
        u, v = map(int, input().split())

        if find(u) == find(v):
            print(1)
        else:
            print(0)
    print()