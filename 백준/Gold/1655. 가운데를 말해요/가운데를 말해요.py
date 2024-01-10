import heapq
import sys
input = sys.stdin.readline

N = int(input())

left = []    # max heap
right = []    # min heap

for n in range(N):
    tmp = [int(input())]

    if n > 0:
        tmp.append(-heapq.heappop(left))
        if n > 1:
            tmp.append(heapq.heappop(right))

    tmp.sort()
    heapq.heappush(left, -tmp[0])

    if n > 1:
        heapq.heappush(right, tmp[2])
    
    if n > 0:
        if not n % 2:
            heapq.heappush(left, -tmp[1])
        else:
            heapq.heappush(right, tmp[1])

    print(-left[0])