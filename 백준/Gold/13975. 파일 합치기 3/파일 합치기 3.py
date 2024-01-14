import heapq

T = int(input())

for t in range(T):
    K = int(input())
    lst = list(map(int, input().split()))

    heapq.heapify(lst)

    result = 0

    while len(lst) > 1:
        tmp = heapq.heappop(lst) + heapq.heappop(lst)
        result += tmp
        heapq.heappush(lst, tmp)

    print(result)