import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()

q = []

for n in range(N):
    if q:
        tmp = heapq.heappop(q)

        if lst[n][0] < tmp:
            heapq.heappush(q, tmp)
    heapq.heappush(q, lst[n][1])

print(len(q))