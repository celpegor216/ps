# 해답: https://ddingmin00.tistory.com/31

import heapq

V, E = map(int, input().split())
lst = [dict() for _ in range(V + 3)]

for _ in range(E):
    a, b, c = map(int, input().split())

    lst[a][b] = min(lst[a].get(b, 21e8), c)
    lst[b][a] = min(lst[b].get(a, 21e8), c)

M, MV = map(int, input().split())
macs = list(map(int, input().split()))
MAC = V + 1    # 모든 맥도날드와 연결된 가상의 노드

S, SV = map(int, input().split())
stars = list(map(int, input().split()))
STAR = V + 2    # 모든 스타벅스와 연결된 가상의 노드

# 가상의 노드에 연결
for mac in macs:
    lst[mac][MAC] = 0
    lst[MAC][mac] = 0

for star in stars:
    lst[star][STAR] = 0
    lst[STAR][star] = 0

MAXV = 21e21
result = MAXV
macs_to_houses = [MAXV] * (V + 3)
stars_to_houses = [MAXV] * (V + 3)

q = []
macs_to_houses[MAC] = 0
heapq.heappush(q, (0, MAC))

while q:
    cost, via = heapq.heappop(q)

    if macs_to_houses[via] < cost:
        continue

    for key, value in lst[via].items():
        next_cost = cost + value

        # 가상의 노드를 지날 수 없음
        if key == MAC or key == STAR:
            continue
        
        if macs_to_houses[key] > next_cost:
            macs_to_houses[key] = next_cost
            heapq.heappush(q, (next_cost, key))

q = []

stars_to_houses[STAR] = 0
heapq.heappush(q, (0, STAR))

while q:
    cost, via = heapq.heappop(q)

    if stars_to_houses[via] < cost:
        continue

    for key, value in lst[via].items():
        next_cost = cost + value

        # 가상의 노드를 지날 수 없음
        if key == MAC or key == STAR:
            continue
        
        if stars_to_houses[key] > next_cost:
            stars_to_houses[key] = next_cost
            heapq.heappush(q, (next_cost, key))

for v in range(1, V + 1):
    if v not in macs and v not in stars and macs_to_houses[v] <= MV and stars_to_houses[v] <= SV:
        result = min(result, macs_to_houses[v] + stars_to_houses[v])

if result == MAXV:
    print(-1)
else:
    print(result)