# 해답: heap의 길이가 n보다 크면 heapq.heappop(heap) 코드로 heap 리스트를 조절

import heapq

N = int(input())

q = []

for n in range(N):
    temp = list(map(int, input().split()))

    for item in temp:
        heapq.heappush(q, item)

        if len(q) > N:
            heapq.heappop(q)

print(heapq.heappop(q))