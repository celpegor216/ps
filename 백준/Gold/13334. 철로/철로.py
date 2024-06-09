# 힌트: 우선순위 큐
# 해답: https://velog.io/@youngeui_hong/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-13334%EB%B2%88-%EC%B2%A0%EB%A1%9C

import heapq

N = int(input())
lst = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    if a > b:
        a, b = b, a
    lst.append((a, b))

D = int(input())

lst.sort(key=lambda x: (x[1], x[0]))

q = []
result = 0

for start, end in lst:
    if end - start > D:
        continue

    heapq.heappush(q, start)
    while q and q[0] + D < end:
        heapq.heappop(q)
    result = max(result, len(q))

print(result)