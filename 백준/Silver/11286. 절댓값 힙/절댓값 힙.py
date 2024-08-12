import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    num = int(input())

    if not num:
        print(heapq.heappop(q)[1] if q else 0)
    else:
        heapq.heappush(q, (abs(num), num))