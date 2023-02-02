# 경로를 찾으려면 목적지에서 가장 가까운 노드를 구하고, 그 노드에서 가장 가까운 노드를 찾는 과정을 시작 노드가 나올 때까지 반복해야 함
# 해답: https://ku-hug.tistory.com/130

import heapq, sys

input = sys.stdin.readline

N = int(input())
M = int(input())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    s, e, c = map(int, input().split())
    
    lst[s].append((e, c))
    
S, E = map(int, input().split())

q = []
heapq.heappush(q, (0, S))

INF = 10e8
result = [INF] * (N + 1)
result[S] = 0
nearest = [S] * (N + 1)    # 해당 인덱스 노드에서 가장 가까운 노드

while q:
    start_via_cost, via = heapq.heappop(q)
    if start_via_cost > result[via]:
        continue
    
    for target, cost in lst[via]:
        start_via_target_cost = start_via_cost + cost
        if start_via_target_cost < result[target]:
            result[target] = start_via_target_cost
            nearest[target] = via
            heapq.heappush(q, (start_via_target_cost, target))

resultlst = []

temp = E
while temp != S:
    resultlst.append(temp)
    temp = nearest[temp]
    
resultlst.append(temp)

print(result[E])
print(len(resultlst))
print(*resultlst[::-1])