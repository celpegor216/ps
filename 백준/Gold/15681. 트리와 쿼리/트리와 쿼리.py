# 루트의 번호가 R인데 첫 번째 쿼리로 잘못 이해함

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

N, R, Q = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for n in range(N - 1):
    U, V = map(int, input().split())

    lst[U].append(V)
    lst[V].append(U)

used = [0] * (N + 1)
def makeTree(num):
    used[num] = 1

    for item in lst[num]:
        if not used[item]:
            used[num] += makeTree(item)
    
    return used[num]

makeTree(R)

for q in range(Q):
    num = int(input())
    print(used[num])