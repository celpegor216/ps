import heapq
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    lst = []

    M = N // 10
    M = M + 1 if N % 10 else M
    for m in range(M):
        lst += list(map(int, input().split()))

    left = []
    right = []
    result = []

    for n in range(N):
        tmp = [lst[n]]
        cnt = 1

        if left:
            tmp.append(-heapq.heappop(left))
            cnt += 1
        if right:
            tmp.append(heapq.heappop(right))
            cnt += 1
        
        tmp.sort()

        heapq.heappush(left, -tmp[0])
        if cnt == 2:
            heapq.heappush(right, tmp[1])
        elif cnt == 3:
            if len(left) == len(right) + 2:
                heapq.heappush(right, tmp[1])
            else:
                heapq.heappush(left, -tmp[1])
            heapq.heappush(right, tmp[2])
                
        if not n % 2:

            if cnt == 1:
                result.append(tmp[0])
            else:
                result.append(tmp[1])
    
    length = len(result)
    print(length)
    for i in range(length):
        print(result[i], end=' ')
        if i != length - 1 and not (i + 1) % 10:
            print()
    print()