# 반례 참고

import sys
input = sys.stdin.readline


N = int(input())
lst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
orders = list(map(int, input().split()))


def find():
    if orders[0] != 1:
        return 0

    parent_idx = 0
    child_idx = 1
    while parent_idx < child_idx and child_idx < N:
        if orders[child_idx] in lst[orders[parent_idx]]:
            child_idx += 1
        else:
            parent_idx += 1
    
    if child_idx != N:
        return 0
    return 1


print(find())