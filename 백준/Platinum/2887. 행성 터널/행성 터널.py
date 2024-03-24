# 메모리 초과
# 해답: https://velog.io/@mingsound21/%EB%B0%B1%EC%A4%80Python-2887-%ED%96%89%EC%84%B1-%ED%84%B0%EB%84%90

import heapq
import sys
input = sys.stdin.readline

N = int(input())
lstx, lsty, lstz = [], [], []
for n in range(N):
    x, y, z = map(int, input().split())
    lstx.append((x, n))
    lsty.append((y, n))
    lstz.append((z, n))

lstx.sort()
lsty.sort()
lstz.sort()

q = []

# 가능한 모든 간선을 저장해서 메모리 초과가 발생함 (N * (N - 1) / 2)
# -> 각 축 별로 위치 정보를 담고, 정렬한 다음, 가장 가까운 간선만 저장 (3 * (N - 1))
for lst in lstx, lsty, lstz:
    for n in range(N - 1):
        heapq.heappush(q, (abs(lst[n + 1][0] - lst[n][0]), lst[n][1], lst[n + 1][1]))

group = [x for x in range(N)]
result = 0

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b, c):
    global result

    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        result += c
        if group_a < group_b:
            group[group_b] = group_a
        else:
            group[group_a] = group_b

while q:
    c, a, b = heapq.heappop(q)

    union(a, b, c)

print(result)