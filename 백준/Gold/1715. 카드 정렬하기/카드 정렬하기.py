import heapq

N = int(input())
p = []
q = []

for n in range(N):
    heapq.heappush(q, int(input()))

result = 0
while len(p) + len(q) > 1:
    ts = [21e8] * 4

    for i in range(2):
        if p:
            ts[i] = heapq.heappop(p)

    for i in range(2):
        if q:
            ts[i + 2] = heapq.heappop(q)
    
    minvs = [ts[0] + ts[1], ts[0] + ts[2], ts[2] + ts[3]]
    minv = min(minvs)
    
    if minv == minvs[0]:
        if ts[2] != 21e8:
            heapq.heappush(q, ts[2])
        if ts[3] != 21e8:
            heapq.heappush(q, ts[3])
    elif minv == minvs[1]:
        if ts[1] != 21e8:
            heapq.heappush(p, ts[1])
        if ts[3] != 21e8:
            heapq.heappush(q, ts[3])
    elif minv == minvs[2]:
        if ts[0] != 21e8:
            heapq.heappush(p, ts[0])
        if ts[1] != 21e8:
            heapq.heappush(p, ts[1])
    result += minv
    heapq.heappush(p, minv)

print(result)