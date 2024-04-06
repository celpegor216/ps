# 세그먼트 트리로 풀었는데 틀림
# 해답: https://velog.io/@veonico/%EB%B0%B1%EC%A4%80-10775.-%EA%B3%B5%ED%95%AD-%ED%8C%8C%EC%9D%B4%EC%8D%ACpython

import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
lst = [int(input()) for _ in range(P)]

group = list(range(G + 1))

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a < group_b:
        group[group_b] = group_a
    else:
        group[group_a] =  group_b

result = 0

for a in lst:
    root = find(a)

    if root == 0:
        break

    union(root, root - 1)
    result += 1

print(result)