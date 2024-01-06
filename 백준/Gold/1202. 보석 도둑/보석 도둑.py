# 이분탐색 같은데 풀이를 모르겠음
# 해답: https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-1202-%EB%B3%B4%EC%84%9D-%EB%8F%84%EB%91%91-Python

import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

jewel = []    # 무게가 작은, 가치가 작은 순서대로 나옴
for n in range(N):
    heapq.heappush(jewel, list(map(int, input().split())))

bag = [int(input()) for _ in range(K)]
bag.sort()

result = 0
tmp = []    # 현재 가방에 들어갈 수 있으면서, 가치가 큰 순서대로 나옴
for b in bag:
    while jewel and b >= jewel[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewel)[1])
    
    if tmp:
        result -= heapq.heappop(tmp)
    elif not jewel:
        break

print(result)